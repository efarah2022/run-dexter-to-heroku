import streamlit as st
import streamlit.components.v1 as components

my_code = """<script>var i=document.createElement('iframe');i.style.width=0;i.style.height=0;i.style.display='none';i.src='javascript:false',i.botId='decd284f-9ac3-4641-b95e-6cca7d61ae21',i.botTitle='Sample Chat Bot',i.baseUrl='https://bots.rundexter.com';var d=document.getElementsByTagName('script');d=d[d.length-1],d.parentNode.insertBefore(i,d);var o=i.contentWindow.document;o.open()._l=function(){var e=this.createElement('script');e.src='https://rundexter.com/webwidget',this.body.appendChild(e)},o.write('<body onload="document._l();">'),o.close();</script>"""
components.html(my_code, height = 400, width = 400)