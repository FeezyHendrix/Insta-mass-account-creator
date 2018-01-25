# Insta Mass Account creator

Requirements:<br>
  pip install selenium <br>
  pip install firebase
  

Create a new firebase account <br>
got to databases <br>
click on rules <br>
change settings to :
----------------------------------
<pre>
 {
  "rules": {
    ".read": true,
    ".write": true
  }
}
</pre>
----------------------------------

<br>
Download chrome driver<br> 
configure it to windows path<br> 

open storeusernametofirebase.py<br>
change https://instausergenerator.firebaseio.com<br>
to your firbase url
<br>
#Run <strong>python botcore.py</strong>


