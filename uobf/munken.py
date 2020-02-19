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
tasks = []


async def post_call(payload):
    try:
        async with sem, session.post(webhook, data=payload, timeout=3600) as response:
            return await response.read()
    except aiohttp.client_exceptions.ClientConnectorError as exc:
        return exc


async def main():
    if time == '10':
        payload = {'text': '@channel Välkomna bröder! Om 5 minuter öppnar det absolut första UÖBF. Jag är Munken och kommer ta hand om er under dagen och uppdatera er om events. Önskar er alla en härlig smakupplevelse!', 'link_names': 1, 'channel': '#test-messages', 'icon_emoji': ':kapittel:', 'username': 'Munken'}
        response = await post_call(json.dumps(payload))
        print(response)

    if time == '11':
        payload = {'text': '@channel Munken meddelar att det endast är 10 minuter kvar till första eventet för dagen. *Vertikaltasting 1*.', 'link_names': 1, 'channel': '#test-messages', 'icon_emoji': ':kapittel:', 'username': 'Munken'}
        response = await post_call(json.dumps(payload))
        print(response)

    elif time == '13':
        payload = {'text': '@channel Dagens andra event gror runt hörnet. Se till att era glas är tomma! *Vertikaltasting 2*.', 'link_names': 1, 'channel': '#test-messages', 'icon_emoji': ':kapittel:', 'username': 'Munken'}
        response = await post_call(json.dumps(payload))
        print(response)

    elif time == '15':
        payload = {'text': '@channel Gammalt är godast, därav kommer det vara ett *blindtest* av gammal gueuze om 10 minuter!', 'link_names': 1, 'channel': '#test-messages', 'icon_emoji': ':kapittel:', 'username': 'Munken'}
        response = await post_call(json.dumps(payload))
        print(response)

    elif time == '18':
        payload = {'text': '@channel Munken har inte fått nog! Spela era dryckesbiljetter väl under *Vertikaltasting 3* om 10 minuter.', 'link_names': 1, 'channel': '#test-messages', 'icon_emoji': ':kapittel:', 'username': 'Munken'}
        response = await post_call(json.dumps(payload))
        print(response)

    elif time == '20':
        payload = {'text': '@channel Vad vore en Öl och Bärs Festival utan en *""Smakupplevelse""*? Vi får se.', 'link_names': 1, 'channel': '#test-messages', 'icon_emoji': ':kapittel:', 'username': 'Munken'}
        response = await post_call(json.dumps(payload))
        print(response)

    elif time == '22':
        payload = {'text': '@channel *Vertikaltasting 3* om tio minuter, vad har vi ens kvar att dricka?', 'link_names': 1, 'channel': '#test-messages', 'icon_emoji': ':kapittel:', 'username': 'Munken'}
        response = await post_call(json.dumps(payload))
        print(response)

    elif time == '23':
        payload = {'text': '@channel Äntligen dags för det vi alla väntat på *Kollens Surprise*. Riktig öl för rktiga munkar!', 'link_names': 1, 'channel': '#test-messages', 'icon_emoji': ':kapittel:', 'username': 'Munken'}
        response = await post_call(json.dumps(payload))
        print(response)

    elif time == '00':
        payload = {'text': '@channel Munken tackar för sig och önksar Kollen en god natt. Tack för att ni besökte *UÖBF1*, vi ses nästa år!', 'link_names': 1, 'channel': '#test-messages', 'icon_emoji': ':kapittel:', 'username': 'Munken'}
        response = await post_call(json.dumps(payload))
        print(response)


if __name__ == '__main__':
    loop.run_until_complete(main())
    loop.close()
