FROM openjdk:17-jdk-alpine

WORKDIR /app

COPY game.java .

# Компилируем Java-файл
RUN javac game.java

CMD ["java", "game"]
