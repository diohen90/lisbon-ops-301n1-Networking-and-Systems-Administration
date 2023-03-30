#!/bin/bash

# Define the log files to be compressed
LOG_FILES="/var/log/journal /var/log/auth.log"

# Create the backup directory if it does not exist
BACKUP_DIR="/var/log/backups"
if [ ! -d $BACKUP_DIR ]; then
  mkdir $BACKUP_DIR
fi

# Loop through each log file and perform the required actions
for FILE in $LOG_FILES; do

  # Print the size of the log file
  echo "File size before compression:"
  du -h $FILE

  # Compress the log file with a timestamped filename
  TIMESTAMP=$(date +%Y%m%d%H%M%S)
  COMPRESSED_FILE="$BACKUP_DIR/$(basename $FILE)-$TIMESTAMP.zip"
  zip -r $COMPRESSED_FILE $FILE

  # Clear the contents of the log file
  > $FILE

  # Print the size of the compressed file
  echo "File size after compression:"
  du -h $COMPRESSED_FILE

  # Compare the size of the original log file to the compressed file
  echo "Compression ratio:"
  ORIGINAL_SIZE=$(du -b $FILE | awk '{print $1}')
  COMPRESSED_SIZE=$(du -b $COMPRESSED_FILE | awk '{print $1}')
  RATIO=$(echo "scale=2; $COMPRESSED_SIZE / $ORIGINAL_SIZE * 100" | bc)
  echo "$RATIO%"
done
