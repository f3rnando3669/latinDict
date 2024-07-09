from typing import List
import Clients.AbstractClient as AbstractClient
from Prompts.PromptList import PromptList
from Prompts.SimplePrompt import SimplePrompt
from openai import OpenAI
from Clients.Utilities.FileUtilities import write_tofile_indir, write_tojson
from Clients.Utilities.StringValidation import emptyString

class ContextTightClient(AbstractClient.ABsClient):
    """
    This is a more powerful Client\n
    You can load context into this model\n
    After getting a response it also saves the information as the last bit of context
    """
    def __init__(self, client: OpenAI, model: str) -> None:
        self._client = client
        self._model = model
        self._context = []

    def loadcontext(self, context: str) -> None:
        """
        load context into the model as a string
        """
        self._context = [context]

    def loadcontext_fromjson(self, jsonobject: List[str], flag=-1) -> None:
        """
        load context into model as a List of strings\n
        By default flag is set as -1, this would make the client always use the most recent context\n
        Flag 0 would get you the first bit of context\n
        Flag 1 would combine all context
        """
        try:
            if flag == 1:
                context = []
                for bit_ofcontext in jsonobject:
                    context.append(bit_ofcontext+"\n")
                self._context = context
            elif flag == 0 or flag == -1:
                context = jsonobject[flag]
                self._context.append(context)
            else:
                raise Exception("Invalid Load Flag")
        except:
            raise Exception("Error whilst reading JSON object!")
    
    def clearcontext(self):
        """
        delete all context
        """
        self._context.clear()
    
    def generate(self, prompts: PromptList, txt_savepath: str="", json_savepath: str="") -> str:
        """
        Enter a list of prompts\n
        You may also specify a savepath for a txt file\n
        Or a savepath for a json file
        """
        context = "\n".join(self._context)
        
        messages = prompts.unpack()
        messages[-1]["content"] = context +"\n"+ messages[-1]["content"]

        generated = self._client.chat.completions.create(
            messages=messages,
            model=self._model
        )
        response = generated.choices[0].message.content
        
        if not emptyString(txt_savepath):
            self._txtsave(txt_savepath, response)

        if not emptyString(json_savepath):
            jsonbuild = self._context + ["".join(messages[-1]["content"])+"\n"+response]
            self._jsonsave(json_savepath, jsonbuild)

        self._context = jsonbuild
        return response

    def _txtsave(self, path, data) -> None:
        write_tofile_indir(path, data)
    
    def _jsonsave(self, path, data):
        write_tojson(path, data)