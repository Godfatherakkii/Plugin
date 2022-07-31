FROM godfatherakkii/GODFATHERBOT:latest

RUN git clone https://github.com/LEGEND-LX/PluginGod.git /root/PluginGod

WORKDIR /root/PluginGod

RUN pip3 install -U -r requirements.txt

ENV PATH="/home/PluginGod/bin:$PATH"

CMD ["python3", "-m", "PluginGod"]
