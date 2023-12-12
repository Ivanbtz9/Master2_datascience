import asyncio # asyncio qui est utilisée pour gérer les opérations asynchrones,

addr = "127.0.0.1"
port = 1234

async def handle(reader, writer): #une coroutine qui gère chaque connexion entrante. 
  data = await reader.read(100) 
  print(f"réception de : {data.decode()}") 

  response = "je suis le serveur et voici ma reponse"
  writer.write(response.encode()) 
  await writer.drain() 
  print(f"envoi de : {response}")

  writer.close()

async def main(addr,port):
  server = await asyncio.start_server(handle,addr,port) 

  async with server:
    await server.serve_forever() 

asyncio.run(main(addr,port))  