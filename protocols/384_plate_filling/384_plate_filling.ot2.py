from opentrons import instruments, labware

# trough and 384-well plate
trough = labware.load('trough-12row', '4', 'trough')
plate = labware.load('384-plate', '2', 'plate')

# 8-channel 10uL pipette, with tip rack and trash
tiprack = labware.load('tiprack-200ul', '1', 'p200rack')

m200 = instruments.P300_Multi(
    mount='left',
    tip_racks=[tiprack],
)


def run_custom_protocol(well_volume: float=30.0):
    alternating_wells = []
    for column in plate.columns():
        alternating_wells.append(column.wells('A', length=8, step=2))
        alternating_wells.append(column.wells('B', length=8, step=2))

    m200.distribute(well_volume, trough.wells('A1'), alternating_wells)
