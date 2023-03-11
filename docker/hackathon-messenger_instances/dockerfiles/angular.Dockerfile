FROM node:16
WORKDIR /usr/src/app/
COPY ./frontend/ ./
RUN npm config set fetch-retry-mintimeout 20000 \
&& npm config set fetch-retry-maxtimeout 120000 \
&& npm install --prefer-offline --no-audit -g @angular/cli @angular-devkit/build-angular && \
npm install --prefer-offline --no-audit
EXPOSE 4200
CMD ["npm", "start"]
