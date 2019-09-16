FROM python
COPY . .
RUN rm -f state.db
RUN echo "#!/bin/bash\necho ''" > /usr/bin/code
RUN chmod +x /usr/bin/code
ENTRYPOINT python index.py

