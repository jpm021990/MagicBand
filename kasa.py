import asyncio
from kasa import SmartPlug

async def main():
    plug = SmartPlug("127.0.0.1")

    await plug.update() #(get latest state)

    if plug.is_on:
      await plug.turn_off()

  if plug.is_off:
    await plug.turn_on()

if __name__ == "__main__":
    asyncio.run(main())
