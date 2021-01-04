# web_content
force for find web content 

# useage

$ ./web_content.py http://www.baidu.com -w /tmp/wordlist.txt -o save.txt -e html -only 200  
output will be  

http://www.baidu.com/!.html 404  
http://www.baidu.com/!_archives.html 404  
http://www.baidu.com/!_images.html 404  
http://www.baidu.com/!backup.html 404  

save file on the current directory
will be save.txt  
and only 200 statu code will in the save.txt file  
if -only option no in use,will save all status code of the web content

$ ./web_content.py --help  
Usage: web_content.py [OPTIONS] URL  

Options:  
  -w TEXT     use wordlist to force  
  -e TEXT     specific file extension to force: example use -e xml will be  
              force http://url/wordlist.xml  

  -o TEXT     save file  
  -only TEXT  choce one of them to save web content, such 200,300,400,500  
  --help      Show this message and exit.  
