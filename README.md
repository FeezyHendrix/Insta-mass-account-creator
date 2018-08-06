# Insta Mass Account creator

Create a new virtual env

- Requirements:<br>
  - run `pip install -r requirements.txt`
  - create a new firebase account <br>
  - got to databases <br>
  - click on rules <br>
  
Change Settings to
```
 {
  "rules": {
    ".read": true,
    ".write": true
  }
}
```
<br>
Download chrome driver<br> 
configure it to path<br> 

## Configuration
open config.py in modules

| Config | Usage |
| :---         |  :---     |
| password | General for Each account generated to be able to login |
| firebase_url | the url to the firebase database |
| proxy_server | proxy server to tunnel browser |
| has_proxy_file | True or False |
| proxy_server_txt_file_path | Path to the proxy file .txt format |
| profile_per_proxy | amount of acccount to be generated for each proxy in the file |
| amount of run | amount of time the code should run |


### Run <strong>python botcore.py</strong>


Fill <a href="https://goo.gl/forms/ZgL8r2DjuaM7xl9R2">Forms</a> to Request for more features


