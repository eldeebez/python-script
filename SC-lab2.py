import sys
import logging

logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='log txt', encoding='UTF-8')
logging.info('the variables are getting initialized')

largestResource = None
failedRequests = 0
totalBytes = 0
totalRequests = 0
totalWaitingTime = 0

logging.info('the loop is getting prapared...')

for line in sys.stdin:
  logging.debug("Check if the line splitted correctly")
  lineInfo = line.split(" ")
  totalBytes += int(lineInfo[2])
  totalRequests+=1
  totalWaitingTime+=int(lineInfo[3])
  logging.debug("Check if the information was added correctly")

  if(largestResource == None or lineInfo[3] > largestResource[3]):
    largestResource = lineInfo 
  
  if lineInfo[1] == "404":
    failedRequests += 1
    print("!", end="")
    logging.debug("Check if the '!' was used correctly")
  
  print(lineInfo[0])


print("")
print("Largest resource path and it's processing time: ", end="")
print(largestResource[0],",", largestResource[3])
print("Number of failed requests:",failedRequests)
print("Number of total bytes sent to a user:",str(totalBytes))
print("Number of total kilobytes sent to a user:",str(totalBytes/1024))
print("Average processing time of a request:",str(totalWaitingTime/totalRequests))
