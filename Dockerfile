FROM ubuntu:latest

# Set environment variable for Discord bot token
ENV DISCORD_TOKEN=$DISCORD_TOKEN

ENV PORT=$PORT
WORKDIR /app
# Install dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip ffmpeg wget && \
#    apt install -y open-jtalk open-jtalk-mecab-naist-jdic ffmpeg && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/freyacodes/Lavalink/releases/download/3.7.5/Lavalink.jar
# Copy the Discord bot files to the container
COPY . /app

# Install Python dependencies
RUN pip3 install -r /app/requirements.txt

# Set the working directory


# Set the DISCORD_TOKEN environment variable before running the bot
#CMD ["bash", "-c", "java -jar Lavalink.jar &; export DISCORD_TOKEN=$DISCORD_TOKEN && python3 main.py"]
RUN chmod 744 /app/start.sh

CMD ["./start.sh"]