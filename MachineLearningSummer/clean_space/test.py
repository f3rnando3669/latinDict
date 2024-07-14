from Clients.ClientInterface import ClientInterface
from Clients.ContextFreeClient import ContextFreeClient
from Clients.ContextTightClient import ContextTightClient
from Prompts.Prompt import Prompt
from Prompts.PromptList import PromptList
from Prompts.SimplePrompt import SimplePrompt
from Clients.Utilities.FileUtilities import readjson, readfile, write_to_file

# Testing ContextTight Client
# text = readfile(r"/home/ml/Computer-Science-Research-Summer/MachineLearningSummer/clean_space/text.txt")
# prompt = SimplePrompt(text)
# prompt2 = SimplePrompt("Apply (Apply <A> to <C>) to \"You must avoid medical doctors when ill because otherwise you will become lazy.\"")
# # prompt3 = SimplePrompt("Apply <C> to <h>")
# prompts = PromptList()
# prompts.add_userprompts([prompt, prompt2])
# client_interface = ClientInterface(ContextTightClient)
# # jsonp = r"/home/ml/Computer-Science-Research-Summer/MachineLearningSummer/clean_space/responsehistory.json"
# tpath = r"/home/ml/Computer-Science-Research-Summer/MachineLearningSummer/clean_space/"
# client_interface._client.generate(prompts=prompts, txt_savepath=tpath, txt_name = "response")

# Testing ContextTight Client and json writing 
# prompt = SimplePrompt()
# prompt.setprompt("How are you?")
# prompts = PromptList()
# prompts.add_userprompt(prompt)
# client = ClientInterface(client=ContextTightClient)._client
# jsonloaded = readjson("jsontext.json")
# client.loadcontext_fromjson(jsonloaded)
# response = client.generate(prompts=prompts, json_savepath="jsontext.json")
# print(response)
# newjson = readjson("jsontext.json")
# print(newjson)

# r = readjson("jsontext.json")
# write_to_file("response", r[-1])

# # Liam's Experiment

parameters = readfile(r"C:\Users\Liam\Desktop\Summer Research\Computer-Science-Research-Summer\MachineLearningSummer\clean_space\sentence_parameter.txt")

parameter_set = SimplePrompt(parameters)
sent_1 = SimplePrompt("Apply <Full_Sent> to the string \'Because the soup was too cold, I warmed it in the microwave\'")

prompts = PromptList()

prompts.add_userprompts([parameter_set, sent_1])

client_interface = ClientInterface(ContextTightClient)
tpath = r"C:\Users\Liam\Desktop\Summer Research\Computer-Science-Research-Summer\MachineLearningSummer\clean_space"
client_interface._client.generate(prompts=prompts, txt_savepath=tpath, txt_name = "response")

# Andi's Experiment
# params = readfile(r"/home/andi/summer2024/Computer-Science-Research-Summer/MachineLearningSummer/rule_book_bank/RAW_Rulebooks_14.txt")
# param_prompt = SimplePrompt(params)
# prompt = SimplePrompt("Apply <IDAA> to \"You should eat more vegetables because they are green\"")
# prompts = PromptList()
# prompts.add_userprompts([param_prompt, prompt])
# client_interface = ClientInterface(ContextTightClient)
# tpath = r"/home/andi/summer2024/Computer-Science-Research-Summer/MachineLearningSummer/clean_space"
# client_interface._client.generate(prompts=prompts, txt_savepath=tpath, txt_name = "response")