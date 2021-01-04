# web_content
force for find web content 

# useage

$ ./web_content.py http://www.baidu.com -w /tmp/wordlist.txt -o save.txt -e html -only 200  

$ ./web_content.py --help  
Usage: web_content.py [OPTIONS] URL  

Options:  
  -w TEXT     use wordlist to force  
  -e TEXT     specific file extension to force: example use -e xml will be  
              force http://url/wordlist.xml  

  -o TEXT     save file  
  -only TEXT  choce one of them to save web content, such 200,300,400,500  
  --help      Show this message and exit.  
