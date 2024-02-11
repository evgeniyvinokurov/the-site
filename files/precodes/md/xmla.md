# xmla v0.3.0
  
Магазин на xml, минимальный прототип проекта  
Python 3 и Bottle.py, чистый джаваскрипт  
  
* /catalog/ - страница каталога  
* /catalog/in/ - страница импорта с мэппингом полей  

структура проекта:  
+-xmla
---codes/xmla - скрипты на питоне  
---views - шаблоны bottle.py  
---static - статика  
---js-src - исходники фронтенда  
---xml - файлы xml  
---imports - каталог для импорта  
---tests - тесты на селениуме    
---for tests - файлы импорта товаров с картинками (тестовые)
    
Проект может работать с докер:  
--исправить index.py (порты)   
--sudo docker build -t xmla .  
--sudo docker run -p 8000:8000 -d xmla  
или  
docker compose up  
