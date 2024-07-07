# Use the official Node.js 20 image as the base image
FROM node:20

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY ./package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY . .

# Set environment variable
RUN JWT_SECRET=$(openssl rand -base64 32) && \
    echo "JWT_SECRET=${JWT_SECRET}" > .env

# Expose the port that the application will listen on
EXPOSE 5001

# Start the application
CMD ["npm", "start"]