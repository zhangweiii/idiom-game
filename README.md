# idiom-game

成语答案生成

体验地址 [demo](http://idiom.zhangwei.ink)

## 安装依赖

1. pip install poetry

2. poetry install

## 以命令行方式运行

1. python .\run.py 都案杯没头盘异扇狼姓块枕草藉温衾

    > ['都头异姓', '头没杯案', '杯盘狼藉', '扇枕温衾', '温衾扇枕', '藉草枕块']

## 部署为网站

1. gunicorn app:app -c gunicorn.conf.py

2. 访问`http://localhost:5000/`

## 以docker方式部署

1. docker build --no-cache -t 'idiom' . 

2. docker run -it --rm -p 5000:5000 idiom

3. 访问`http://localhost:5000/`
