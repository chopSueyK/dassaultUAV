from mavsdk import System
import asyncio
async def run():
        
    drone = System()
    await drone.connect(system_address="udp://:14540")
    