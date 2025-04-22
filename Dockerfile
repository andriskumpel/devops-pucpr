FROM alpine:latest

RUN echo '#!/bin/sh' > /app.sh && \
    echo 'echo "Aplicação rodando dentro do container!"' >> /app.sh

RUN chmod +x /app.sh

CMD ["/app.sh"]
