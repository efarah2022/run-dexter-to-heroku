"""Heroku Deployer

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xJhI5_4ItKnpUIwliKxlDVJV9-JV8chh
"""
from pyngrok import ngrok
def launch_website():
  print ("Click this link to try your web app:")
  print ("If you get an error, wait 5 seconds and click again!")
  public_url = ngrok.connect(port='80')
  print (public_url)
  # !streamlit run --server.port 80 app.py >/dev/null

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
import streamlit as st
import streamlit.components.v1 as components

my_code = """<script>var i=document.createElement('iframe');i.style.width=0;i.style.height=0;i.style.display='none';i.src='javascript:false',i.botId='decd284f-9ac3-4641-b95e-6cca7d61ae21',i.botTitle='Sample Chat Bot',i.baseUrl='https://bots.rundexter.com';var d=document.getElementsByTagName('script');d=d[d.length-1],d.parentNode.insertBefore(i,d);var o=i.contentWindow.document;o.open()._l=function(){var e=this.createElement('script');e.src='https://rundexter.com/webwidget',this.body.appendChild(e)},o.write('<body onload="document._l();">'),o.close();</script>"""
components.html(my_code, height = 400, width = 400)

# launch_website()