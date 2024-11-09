FROM dart:stable

WORKDIR /app

COPY calc.dart .

RUN dart compile exe calc.dart -o calc

CMD ["./calc"]
