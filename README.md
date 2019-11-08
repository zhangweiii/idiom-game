# idiom-game

成语答案生成

1. pip install poetry

2. poetry install

3. python .\run.py 都案杯没头盘异扇狼姓块枕草藉温衾

    > ['都头异姓', '头没杯案', '杯盘狼藉', '扇枕温衾', '温衾扇枕', '藉草枕块']

4. docker build --no-cache -t 'idiom' . 

5. docker run -it --rm -p 5000:5000 idiom

6. 访问`http://localhost:5000/`


> 其中第三条是命令行执行，4至6是部署为网站