import string

def automate_input_file_json(file_name):
    pre_method_text = """{"custom_id": "request-"""
        
    pre_user_content_text = """","method": "POST","url": "/v1/chat/completions","body": {"model": "gpt-4o-mini","messages": [{"role": "developer", "content": "Your responce must be a valid JSON format."},{"role": "user", "content": "All the companies listed on National Stock Exchange (NSE) India, starting with the charecter """
    post_user_content_text = """ in Json format with the following attributes, 'name, description, type'. Name - name of company, description - must include short description of company information, their main source of revenue, current holdings, what does company do? in less than 50 words. type - give a label to company according to its type, like bank, technology, pharma, telecom, etc."}],"max_tokens": 1000000} }"""
    for i in range(65,91):
        charecter = chr(i)
        final = pre_method_text + charecter + pre_user_content_text + charecter + post_user_content_text
        with open(file_name,'a') as f:
            f.write(final+"\n")
            
            