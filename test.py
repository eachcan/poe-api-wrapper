from poe_api_wrapper import PoeApi
import unittest, random, string
import logging

logging.getLogger('poe_api_wrapper').setLevel(logging.WARNING)

# p_b = input("Enter your p-b cookie: ")
# p_lat = input("Enter your p-lat cookie: ")
p_b = 'WVvoFBfoBzvuDbxDvbWbqQ=='
p_lat = 'ORNVxWGDPNY7JbojoOMXx9wozazz0tq73LfgTe6D6Q=='
formkey = '0124d76edadf21ae5d62a593d5a53114'
bm = 'IirrFlaC8P_Vi9KvXGsUQIFtCBgBCCwJIoz6IRFelVs-1746807597-1.0.1.1-6LUq_alIgavtz4aQbrXYXCabFJmJWeaU.Ah.gk3CuVG91AhuLpSNOKAPTZLRCxJMqx_zLIM5xXyAzYTq6WyoJS_Di55bwhxdIyDEUfdCnxc'
cf = 'Cnf2Uh2D64ndOmWCwynJCzYwxrX3gMTq1LI5IFyaMPY-1746803741-1.2.1.1-8Uj_Xy6bCVUUscqN1yG_IZInXzNKYcUonCW68s6x5FZTiRfvH_G09k.47mBdwVayAaod6nxJbiTnQcORO6dhJNNFw6aZF4gbF1AZBnXvZuU4O_8xat8LhJCGbMXKuLYuKHJ8Y.jxln0qEysO6wFDmNnAkvJg9AKDAigLJsox9.MmugtftlElYvx_t.BlQFNVhx.oh_bk2GMX9iKWdHSPMFyE3yW6Jm09mH0T0dFuqyymT_sKRKYNB8U8Cfn9nHeIHI9009.aE4V.z97NyLIZllycOYKaNSnhv0qfW4dvDunlSuYliHhzNVSqP4wyrsOlZNvXaWTjK.XOamwLT3NDv46GnC_OhuKGO9dwKuiEodcQhfEUIzcpDO4arkukldBt'

TOKEN = {
    'p-b': p_b, 
    'p-lat': p_lat, 
    'formkey': formkey,
    '__cf_bm': bm,
    'cf_clearance': cf
}

def testObjectGenerator(length):
       return ''.join(random.choice(string.ascii_letters) for _ in range(length))
   
class PoeApiTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.botName = testObjectGenerator(20)
        cls.botName2 = testObjectGenerator(20)
        print("Initializing tests")
                
    # def test_get_subscription_info(self):
    #     client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
    #     client.get_channel_settings()
    #     client.subscribe()
        
    # def test_get_available_bots(self):
    #     client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
    #     client.get_available_bots()
        
    # def test_get_available_categories(self):
    #     client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
    #     client.get_available_categories()
        
    # def test_get_user_bots(self):
    #     client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
    #     client.get_user_bots(user='poe')
        
    # def test_explore(self):
    #     client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
    #     client.explore(count=10)
    #     client.explore(search="Midjourney", count=30)
    #     client.explore(categoryName="Popular", count=30)
    #     client.explore(search="Poe", entity_type='user', count=30)
        
    # def test_get_chat_history(self):
    #     client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
    #     client.get_chat_history(count=200)
    
    def test_send_message(self):
        client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
        for msg in client.send_message(bot='App-Creator', message='请用中文一句话介绍你的特点，不要废话，直接输出，不要带好的之类的', suggest_replies=True):
            print(msg)
        
    # def test_upload_file(self):
    #     client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
    #     file_urls = ["https://elinux.org/images/c/c5/IntroductionToReverseEngineering_Anderson.pdf", 
    #                 "https://www.kcl.ac.uk/warstudies/assets/automation-and-artificial-intelligence.pdf"]
    #     for _ in client.send_message(bot="a2", message="Compare 2 files and describe them in 100 words", file_path=file_urls):
    #         pass
    
    # def test_get_threadData(self):
    #     client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
    #     client.get_threadData(bot="a2")
    
    # def test_cancel_message(self):
    #     client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
    #     i = 0
    #     for chunk in client.send_message(bot="a2", message="What is the meaning of life (100 words)?"):
    #         i += 1
    #         if i >= 2:
    #             client.cancel_message(chunk)
    #             break 
    # def test_retry_message(self):
    #     client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
    #     for _ in client.send_message(bot="capybara", message="Explain Quantaum Mechanics in 50 words"):
    #         pass
    #     chatCode = client.get_chat_history("capybara")['data']['capybara'][0]['chatCode']
    #     for _ in client.retry_message(chatCode=chatCode):
    #         pass
    
    # def test_clear_conversation(self):
    #     client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
    #     chatCode = client.get_chat_history("a2")['data']['a2'][0]['chatCode']
    #     client.chat_break(bot="a2", chatCode=chatCode)

    # def test_purge_conversation(self):
    #     client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
    #     chatCode = client.get_chat_history("a2")['data']['a2'][0]['chatCode']
    #     client.purge_conversation(bot="a2", chatCode=chatCode)
        
    # def test_get_previous_messages(self):
    #     client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
    #     chatCode = client.get_chat_history("a2")['data']['a2'][0]['chatCode']
    #     client.get_previous_messages('a2', chatCode=chatCode, count=2)
    
    # def test_upload_knowledge(self):
    #     client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
        
    #     # Web urls
    #     file_urls = ["https://elinux.org/images/c/c5/IntroductionToReverseEngineering_Anderson.pdf", 
    #         "https://www.kcl.ac.uk/warstudies/assets/automation-and-artificial-intelligence.pdf"]
    #     client.upload_knowledge(file_path=file_urls)
        
    #     # Text knowledge
    #     knowledges = [
    #         {
    #             "title": "What is Quora?",
    #             "content": "Quora is a popular online platform that enables users to ask questions on various topics and receive answers from a diverse community. It covers a wide range of subjects, from academic and professional queries to personal experiences and opinions, fostering knowledge-sharing and meaningful discussions among its users worldwide."
    #         },
    #         {
    #             "title": "Founders of Quora",
    #             "content": "Quora was founded by two individuals, Adam D'Angelo and Charlie Cheever. Adam D'Angelo, who previously served as the Chief Technology Officer (CTO) at Facebook, and Charlie Cheever, a former Facebook employee as well, launched Quora in June 2009. They aimed to create a platform that would enable users to ask questions and receive high-quality answers from knowledgeable individuals. Since its inception, Quora has grown into a widely used question-and-answer platform with a large user base and a diverse range of topics covered."
    #         },
    #     ]
    #     client.upload_knowledge(text_knowledge=knowledges)
        
    # def test_edit_knowledge(self):
    #     client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
    #     knowledges = [
    #         {
    #             "title": "What is Quora?",
    #             "content": "Quora is a popular online platform that enables users to ask questions on various topics and receive answers from a diverse community. It covers a wide range of subjects, from academic and professional queries to personal experiences and opinions, fostering knowledge-sharing and meaningful discussions among its users worldwide."
    #         },
    #         {
    #             "title": "Founders of Quora",
    #             "content": "Quora was founded by two individuals, Adam D'Angelo and Charlie Cheever. Adam D'Angelo, who previously served as the Chief Technology Officer (CTO) at Facebook, and Charlie Cheever, a former Facebook employee as well, launched Quora in June 2009. They aimed to create a platform that would enable users to ask questions and receive high-quality answers from knowledgeable individuals. Since its inception, Quora has grown into a widely used question-and-answer platform with a large user base and a diverse range of topics covered."
    #         },
    #     ]
    #     source_ids = client.upload_knowledge(text_knowledge=knowledges)
    #     client.edit_knowledge(knowledgeSourceId=source_ids['What is Quora?'][-1], title='What is Quora?', content='Quora is a question-and-answer platform where users can ask questions, provide answers, and engage in discussions on various topics.')

    # def test_create_bot(self):
    #     client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
    #     knowledges = [
    #         {
    #             "title": "What is Quora?",
    #             "content": "Quora is a popular online platform that enables users to ask questions on various topics and receive answers from a diverse community. It covers a wide range of subjects, from academic and professional queries to personal experiences and opinions, fostering knowledge-sharing and meaningful discussions among its users worldwide."
    #         },
    #         {
    #             "title": "Founders of Quora",
    #             "content": "Quora was founded by two individuals, Adam D'Angelo and Charlie Cheever. Adam D'Angelo, who previously served as the Chief Technology Officer (CTO) at Facebook, and Charlie Cheever, a former Facebook employee as well, launched Quora in June 2009. They aimed to create a platform that would enable users to ask questions and receive high-quality answers from knowledgeable individuals. Since its inception, Quora has grown into a widely used question-and-answer platform with a large user base and a diverse range of topics covered."
    #         },
    #     ]
    #     source_ids = client.upload_knowledge(text_knowledge=knowledges)
    #     client.create_bot(handle=self.botName, prompt='You are a helpful assitant', base_model='a2', knowledgeSourceIds=source_ids)
        
    # def test_get_available_knowledge(self):
    #     client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
    #     client.get_available_knowledge(botName=self.botName)
        
    # def test_delete_bot(self):
    #     client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
    #     client.delete_bot(handle=self.botName)
        
    # def test_edit_bot(self):
    #     client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
    #     knowledges = [
    #         {
    #             "title": "What is Quora?",
    #             "content": "Quora is a popular online platform that enables users to ask questions on various topics and receive answers from a diverse community. It covers a wide range of subjects, from academic and professional queries to personal experiences and opinions, fostering knowledge-sharing and meaningful discussions among its users worldwide."
    #         },
    #         {
    #             "title": "Founders of Quora",
    #             "content": "Quora was founded by two individuals, Adam D'Angelo and Charlie Cheever. Adam D'Angelo, who previously served as the Chief Technology Officer (CTO) at Facebook, and Charlie Cheever, a former Facebook employee as well, launched Quora in June 2009. They aimed to create a platform that would enable users to ask questions and receive high-quality answers from knowledgeable individuals. Since its inception, Quora has grown into a widely used question-and-answer platform with a large user base and a diverse range of topics covered."
    #         },
    #     ]
    #     source_ids = client.upload_knowledge(text_knowledge=knowledges)
    #     client.create_bot(handle=self.botName2, prompt='You are a helpful assitant', base_model='a2', knowledgeSourceIds=source_ids)
    #     client.edit_bot(handle=self.botName2, prompt='You are a helpful assitant', base_model='chinchilla', knowledgeSourceIdsToRemove=source_ids)
    #     client.delete_bot(handle=self.botName2)
        
    # def test_shareCode(self):
    #     client = PoeApi(tokens=TOKEN, proxy='http://127.0.0.1:7890')
    #     chatCode = client.get_chat_history("capybara")['data']['capybara'][0]['chatCode']
    #     shareCode = client.share_chat("capybara", chatCode=chatCode, count=2)
    #     client.import_chat("capybara", shareCode=shareCode)
        
unittest.main(verbosity=2)