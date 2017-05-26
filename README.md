# Intest
run django

1.获取当前安装的库，存到requirements.txt
`pip freeze > ./requirements.txt`
2.用requirements.txt安装
`pip install -r ./requirements.txt`

tip
`ImportError: No module named 'sysmon'`
原因是没有安装
`django-system-monitor`