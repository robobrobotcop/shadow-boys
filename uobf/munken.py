# -*- coding: utf-8 -*- 
import json
import random
import aiohttp
import asyncio
import datetime


webhook = ''

time = datetime.datetime.now().strftime("%H")
sem = asyncio.Semaphore(16)
loop = asyncio.get_event_loop()
session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))


async def post_call(payload):
    try:
        async with sem, session.post(webhook, data=payload, timeout=3600) as response:
            return await response.read()
    except aiohttp.client_exceptions.ClientConnectorError as exc:
        return exc


async def message():

    if time == '09':
        payload = {'text': '@channel Välkomna bröder! Om 10 minuter öppnar det absolut första UÖBF. Jag är Munken och kommer ta hand om er under dagen och uppdatera er om evenemang. Önskar er alla en härlig smakupplevelse!', 'link_names': 1, 'channel': '#uobf1', 'icon_emoji': ':kapittel:', 'username': 'Munken'}
        return payload

    elif time == '10':
        payload = {'text': '@channel Munken meddelar att det endast är 10 minuter kvar till första evenemanget för dagen. *Vertikaltasting 1*.', 'link_names': 1, 'channel': '#uobf1', 'icon_emoji': ':kapittel:', 'username': 'Munken'}
        return payload

    elif time == '12':
        payload = {'text': '@channel Dagens andra evenemang gror runt hörnet. Se till att era glas är tomma! *Vertikaltasting 2*.', 'link_names': 1, 'channel': '#uobf1', 'icon_emoji': ':kapittel:', 'username': 'Munken'}
        return payload

    elif time == '14':
        payload = {'text': '@channel Gammalt är godast, därav kommer det vara ett *blindtest* av gammal gueuze om 10 minuter!', 'link_names': 1, 'channel': '#uobf1', 'icon_emoji': ':kapittel:', 'username': 'Munken'}
        return payload

    elif time == '17':
        payload = {'text': '@channel Munken har inte fått nog! Spela era dryckesbiljetter väl under *Vertikaltasting 3* om 10 minuter.', 'link_names': 1, 'channel': '#uobf1', 'icon_emoji': ':kapittel:', 'username': 'Munken'}
        return payload

    elif time == '19':
        payload = {'text': '@channel Vad vore en Öl och Bärs Festival utan en *""Smakupplevelse""*? Vi får se.', 'link_names': 1, 'channel': '#uobf1', 'icon_emoji': ':kapittel:', 'username': 'Munken'}
        return payload

    elif time == '21':
        payload = {'text': '@channel *Vertikaltasting 4* om tio minuter, vad har vi ens kvar att dricka?', 'link_names': 1, 'channel': '#uobf1', 'icon_emoji': ':kapittel:', 'username': 'Munken'}
        return payload

    elif time == '22':
        payload = {'text': '@channel Äntligen dags för det vi alla väntat på *Kollens Surprise*. Riktig öl för riktiga munkar!', 'link_names': 1, 'channel': '#uobf1', 'icon_emoji': ':kapittel:', 'username': 'Munken'}
        return payload

    elif time == '23':
        payload = {'text': '@channel Munken tackar för sig och önskar Kollen en god natt. Tack för att ni besökte *UÖBF1*, vi ses nästa år!', 'link_names': 1, 'channel': '#uobf1', 'icon_emoji': ':kapittel:', 'username': 'Munken'}
        return payload

    else:
        pass


async def main():
    payload = await message()
    
    if payload == '':
        pass
    else:
        await post_call(json.dumps(payload))


if __name__ == '__main__':
    loop.run_until_complete(main())
    session.close()
    loop.close()
