from pyracing import client, helpers, constants
import asyncio
import logging

def custom_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(name)s; %(asctime)s; %(levelname)s; %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename=".\pyracing-logs\client.log",
        filemode='w',
    )
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)s: %(message)s')
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)
    return logging.getLogger()

ir = client.Client('', log=custom_logger())

customer_id = 435144
async def main():
    career = await ir.world_records(2019, 3, 33, 319 )
    print(career[0].__class__.__name__)
    for attr, value in career[0].__dict__.items():
        print(str(attr) + ' | ' +  str(type(value)).replace('<class \'', '').replace('\'>', '') + ' | ' + str(value))


        

    # await ir._authenticate()
    # list_of_season_objects = await ir.current_seasons()

    # for season in list_of_season_objects:
        
    #     if season.series_id == 231:
    #         print(f'\nSchedule for {season.series_name_short}' 
    #                 f' ({season.season_year} S{season.season_quarter})')
            
    #         for t in season.tracks:
    #             print(f'    Week {t.race_week} will take place at {t.name} ({t.config})')

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
fut = loop.create_task(main())
loop.run_until_complete(fut)

# asyncio.run(main())


