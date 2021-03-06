#This class holds all of the messy data
class Properties:

    def __init__(self):
        
        self.BirdFileNames = [ "001.Black_footed_Albatross",
                        "002.Laysan_Albatross",
                        "003.Sooty_Albatross",
                        "004.Groove_billed_Ani",
                        "005.Crested_Auklet",
                        "006.Least_Auklet",
                        "007.Parakeet_Auklet",
                        "008.Rhinoceros_Auklet",
                        "009.Brewer_Blackbird",
                        "010.Red_winged_Blackbird",
                        "011.Rusty_Blackbird",
                        "012.Yellow_headed_Blackbird",
                        "013.Bobolink",
                        "014.Indigo_Bunting",
                        "015.Lazuli_Bunting",
                        "016.Painted_Bunting",
                        "017.Cardinal",
                        "018.Spotted_Catbird",
                        "019.Gray_Catbird",
                        "020.Yellow_breasted_Chat",
                        "021.Eastern_Towhee",
                        "022.Chuck_will_Widow",
                        "023.Brandt_Cormorant",
                        "024.Red_faced_Cormorant",
                        "025.Pelagic_Cormorant",
                        "026.Bronzed_Cowbird",
                        "027.Shiny_Cowbird",
                        "028.Brown_Creeper",
                        "029.American_Crow",
                        "030.Fish_Crow",
                        "031.Black_billed_Cuckoo",
                        "032.Mangrove_Cuckoo",
                        "033.Yellow_billed_Cuckoo",
                        "034.Gray_crowned_Rosy_Finch",
                        "035.Purple_Finch",
                        "036.Northern_Flicker",
                        "037.Acadian_Flycatcher",
                        "038.Great_Crested_Flycatcher",
                        "039.Least_Flycatcher",
                        "040.Olive_sided_Flycatcher",
                        "041.Scissor_tailed_Flycatcher",
                        "042.Vermilion_Flycatcher",
                        "043.Yellow_bellied_Flycatcher",
                        "044.Frigatebird",
                        "045.Northern_Fulmar",
                        "046.Gadwall",
                        "047.American_Goldfinch",
                        "048.European_Goldfinch",
                        "049.Boat_tailed_Grackle",
                        "050.Eared_Grebe",
                        "051.Horned_Grebe",
                        "052.Pied_billed_Grebe",
                        "053.Western_Grebe",
                        "054.Blue_Grosbeak",
                        "055.Evening_Grosbeak",
                        "056.Pine_Grosbeak",
                        "057.Rose_breasted_Grosbeak",
                        "058.Pigeon_Guillemot",
                        "059.California_Gull",
                        "060.Glaucous_winged_Gull",
                        "061.Heermann_Gull",
                        "062.Herring_Gull",
                        "063.Ivory_Gull",
                        "064.Ring_billed_Gull",
                        "065.Slaty_backed_Gull",
                        "066.Western_Gull",
                        "067.Anna_Hummingbird",
                        "068.Ruby_throated_Hummingbird",
                        "069.Rufous_Hummingbird",
                        "070.Green_Violetear",
                        "071.Long_tailed_Jaeger",
                        "072.Pomarine_Jaeger",
                        "073.Blue_Jay",
                        "074.Florida_Jay",
                        "075.Green_Jay",
                        "076.Dark_eyed_Junco",
                        "077.Tropical_Kingbird",
                        "078.Gray_Kingbird",
                        "079.Belted_Kingfisher",
                        "080.Green_Kingfisher",
                        "081.Pied_Kingfisher",
                        "082.Ringed_Kingfisher",
                        "083.White_breasted_Kingfisher",
                        "084.Red_legged_Kittiwake",
                        "085.Horned_Lark",
                        "086.Pacific_Loon",
                        "087.Mallard",
                        "088.Western_Meadowlark",
                        "089.Hooded_Merganser",
                        "090.Red_breasted_Merganser",
                        "091.Mockingbird",
                        "092.Nighthawk",
                        "093.Clark_Nutcracker",
                        "094.White_breasted_Nuthatch",
                        "095.Baltimore_Oriole",
                        "096.Hooded_Oriole",
                        "097.Orchard_Oriole",
                        "098.Scott_Oriole",
                        "099.Ovenbird",
                        "100.Brown_Pelican",
                        "101.White_Pelican",
                        "102.Western_Wood_Pewee",
                        "103.Sayornis",
                        "104.American_Pipit",
                        "105.Whip_poor_Will",
                        "106.Horned_Puffin",
                        "107.Common_Raven",
                        "108.White_necked_Raven",
                        "109.American_Redstart",
                        "110.Geococcyx",
                        "111.Loggerhead_Shrike",
                        "112.Great_Grey_Shrike",
                        "113.Baird_Sparrow",
                        "114.Black_throated_Sparrow",
                        "115.Brewer_Sparrow",
                        "116.Chipping_Sparrow",
                        "117.Clay_colored_Sparrow",
                        "118.House_Sparrow",
                        "119.Field_Sparrow",
                        "120.Fox_Sparrow",
                        "121.Grasshopper_Sparrow",
                        "122.Harris_Sparrow",
                        "123.Henslow_Sparrow",
                        "124.Le_Conte_Sparrow",
                        "125.Lincoln_Sparrow",
                        "126.Nelson_Sharp_tailed_Sparrow",
                        "127.Savannah_Sparrow",
                        "128.Seaside_Sparrow",
                        "129.Song_Sparrow",
                        "130.Tree_Sparrow",
                        "131.Vesper_Sparrow",
                        "132.White_crowned_Sparrow",
                        "133.White_throated_Sparrow",
                        "134.Cape_Glossy_Starling",
                        "135.Bank_Swallow",
                        "136.Barn_Swallow",
                        "137.Cliff_Swallow",
                        "138.Tree_Swallow",
                        "139.Scarlet_Tanager",
                        "140.Summer_Tanager",
                        "141.Artic_Tern",
                        "142.Black_Tern",
                        "143.Caspian_Tern",
                        "144.Common_Tern",
                        "145.Elegant_Tern",
                        "146.Forsters_Tern",
                        "147.Least_Tern",
                        "148.Green_tailed_Towhee",
                        "149.Brown_Thrasher",
                        "150.Sage_Thrasher",
                        "151.Black_capped_Vireo",
                        "152.Blue_headed_Vireo",
                        "153.Philadelphia_Vireo",
                        "154.Red_eyed_Vireo",
                        "155.Warbling_Vireo",
                        "156.White_eyed_Vireo",
                        "157.Yellow_throated_Vireo",
                        "158.Bay_breasted_Warbler",
                        "159.Black_and_white_Warbler",
                        "160.Black_throated_Blue_Warbler",
                        "161.Blue_winged_Warbler",
                        "162.Canada_Warbler",
                        "163.Cape_May_Warbler",
                        "164.Cerulean_Warbler",
                        "165.Chestnut_sided_Warbler",
                        "166.Golden_winged_Warbler",
                        "167.Hooded_Warbler",
                        "168.Kentucky_Warbler",
                        "169.Magnolia_Warbler",
                        "170.Mourning_Warbler",
                        "171.Myrtle_Warbler",
                        "172.Nashville_Warbler",
                        "173.Orange_crowned_Warbler",
                        "174.Palm_Warbler",
                        "175.Pine_Warbler",
                        "176.Prairie_Warbler",
                        "177.Prothonotary_Warbler",
                        "178.Swainson_Warbler",
                        "179.Tennessee_Warbler",
                        "180.Wilson_Warbler",
                        "181.Worm_eating_Warbler",
                        "182.Yellow_Warbler",
                        "183.Northern_Waterthrush",
                        "184.Louisiana_Waterthrush",
                        "185.Bohemian_Waxwing",
                        "186.Cedar_Waxwing",
                        "187.American_Three_toed_Woodpecker",
                        "188.Pileated_Woodpecker",
                        "189.Red_bellied_Woodpecker",
                        "190.Red_cockaded_Woodpecker",
                        "191.Red_headed_Woodpecker",
                        "192.Downy_Woodpecker",
                        "193.Bewick_Wren",
                        "194.Cactus_Wren",
                        "195.Carolina_Wren",
                        "196.House_Wren",
                        "197.Marsh_Wren",
                        "198.Rock_Wren",
                        "199.Winter_Wren",
                        "200.Common_Yellowthroat" ]

        self.BirdSpeciesNames = ['Black footed Albatross', 'Laysan Albatross', 
                                'Sooty Albatross', 'Groove billed Ani',
                                'Crested Auklet', 'Least Auklet',
                                'Parakeet Auklet', 'Rhinoceros Auklet', 
                                'Brewer Blackbird', 'Red winged Blackbird', 
                                'Rusty Blackbird', 'Yellow headed Blackbird', 
                                'Bobolink', 'Indigo Bunting', 
                                'Lazuli Bunting', 'Painted Bunting', 
                                'Cardinal', 'Spotted Catbird', 
                                'Gray Catbird', 'Yellow breasted Chat', 
                                'Eastern Towhee', 'Chuck will Widow', 
                                'Brandt Cormorant', 'Red faced Cormorant', 
                                'Pelagic Cormorant', 'Bronzed Cowbird', 
                                'Shiny Cowbird', 'Brown Creeper', 
                                'American Crow', 'Fish Crow', 
                                'Black billed Cuckoo', 'Mangrove Cuckoo', 
                                'Yellow billed Cuckoo', 'Gray crowned Rosy Finch', 
                                'Purple Finch', 'Northern Flicker', 
                                'Acadian Flycatcher', 'Great Crested Flycatcher', 
                                'Least Flycatcher', 'Olive sided Flycatcher', 
                                'Scissor tailed Flycatcher', 'Vermilion Flycatcher', 
                                'Yellow bellied Flycatcher', 'Frigatebird', 
                                'Northern Fulmar', 'Gadwall', 
                                'American Goldfinch', 'European Goldfinch', 
                                'Boat tailed Grackle', 'Eared Grebe', 
                                'Horned Grebe', 'Pied billed Grebe', 
                                'Western Grebe', 'Blue Grosbeak', 
                                'Evening Grosbeak', 'Pine Grosbeak', 
                                'Rose breasted Grosbeak', 'Pigeon Guillemot', 
                                'California Gull', 'Glaucous winged Gull', 
                                'Heermann Gull', 'Herring Gull', 
                                'Ivory Gull', 'Ring billed Gull', 
                                'Slaty backed Gull',  'Western Gull', 
                                'Anna Hummingbird', 'Ruby throated Hummingbird', 
                                'Rufous Hummingbird', 'Green Violetear', 
                                'Long tailed Jaeger', 'Pomarine Jaeger',
                                'Blue Jay', 'Florida Jay', 
                                'Green Jay', 'Dark eyed Junco', 
                                'Tropical Kingbird', 'Gray Kingbird', 
                                'Belted Kingfisher', 'Green Kingfisher', 
                                'Pied Kingfisher', 'Ringed Kingfisher', 
                                'White breasted Kingfisher', 'Red legged Kittiwake', 
                                'Horned Lark', 'Pacific Loon', 
                                'Mallard', 'Western Meadowlark', 
                                'Hooded Merganser', 'Red breasted Merganser', 
                                'Mockingbird', 'Nighthawk', 
                                'Clark Nutcracker', 'White breasted Nuthatch', 
                                'Baltimore Oriole', 'Hooded Oriole', 
                                'Orchard Oriole', 'Scott Oriole', 
                                'Ovenbird', 'Brown Pelican', 
                                'White Pelican', 'Western Wood Pewee', 
                                'Sayornis', 'American Pipit', 
                                'Whip poor Will', 'Horned Puffin', 
                                'Common Raven', 'White necked Raven', 
                                'American Redstart', 'Geococcyx', 
                                'Loggerhead Shrike', 'Great Grey Shrike', 
                                'Baird Sparrow', 'Black throated Sparrow', 
                                'Brewer Sparrow', 'Chipping Sparrow', 
                                'Clay colored Sparrow', 'House Sparrow', 
                                'Field Sparrow', 'Fox Sparrow', 
                                'Grasshopper Sparrow', 'Harris Sparrow', 
                                'Henslow Sparrow', 'Le Conte Sparrow', 
                                'Lincoln Sparrow', 'Nelson Sharp tailed Sparrow', 
                                'Savannah Sparrow', 'Seaside Sparrow', 
                                'Song Sparrow', 'Tree Sparrow', 
                                'Vesper Sparrow', 'White crowned Sparrow', 
                                'White throated Sparrow', 'Cape Glossy Starling', 
                                'Bank Swallow', 'Barn Swallow', 
                                'Cliff Swallow', 'Tree Swallow', 
                                'Scarlet Tanager', 'Summer Tanager', 
                                'Artic Tern', 'Black Tern', 
                                'Caspian Tern', 'Common Tern', 
                                'Elegant Tern', 'Forsters Tern', 
                                'Least Tern', 'Green tailed Towhee', 
                                'Brown Thrasher', 'Sage Thrasher', 
                                'Black capped Vireo', 'Blue headed Vireo', 
                                'Philadelphia Vireo', 'Red eyed Vireo', 
                                'Warbling Vireo', 'White eyed Vireo', 
                                'Yellow throated Vireo', 'Bay breasted Warbler', 
                                'Black and white Warbler', 'Black throated Blue Warbler', 
                                'Blue winged Warbler', 'Canada Warbler', 
                                'Cape May Warbler', 'Cerulean Warbler', 
                                'Chestnut sided Warbler', 'Golden winged Warbler', 
                                'Hooded Warbler', 'Kentucky Warbler', 
                                'Magnolia Warbler', 'Mourning Warbler', 
                                'Myrtle Warbler', 'Nashville Warbler', 
                                'Orange crowned Warbler', 'Palm Warbler', 
                                'Pine Warbler', 'Prairie Warbler', 
                                'Prothonotary Warbler', 'Swainson Warbler', 
                                'Tennessee Warbler', 'Wilson Warbler', 
                                'Worm eating Warbler', 'Yellow Warbler', 
                                'Northern Waterthrush', 'Louisiana Waterthrush', 
                                'Bohemian Waxwing', 'Cedar Waxwing', 
                                'American Three toed Woodpecker', 
                                'Pileated Woodpecker', 'Red bellied Woodpecker', 
                                'Red cockaded Woodpecker', 'Red headed Woodpecker', 
                                'Downy Woodpecker', 'Bewick Wren', 
                                'Cactus Wren', 'Carolina Wren', 
                                'House Wren', 'Marsh Wren', 
                                'Rock Wren', 'Winter Wren', 'Common Yellowthroat']

        self.missingDataBirdTest =[
                    14, 39, 69, 71, 73, 90, 140, 148, 151, 153, 207, 266, 268, 274, 285, 286,
                    313, 344, 353, 387, 425, 443, 452, 482, 511, 519, 544, 558, 566, 570, 581,
                    592, 609, 668, 716, 744, 777, 784, 785, 814, 828, 870, 871, 887, 926, 938,
                    942, 949, 957, 972, 981, 1011, 1019, 1055, 1103, 1107, 1130, 1133, 1142, 
                    1177, 1179, 1203, 1209, 1225, 1243, 1320, 1327, 1358, 1384, 1394, 1404, 
                    1413, 1422, 1434, 1442, 1451, 1511, 1520, 1528, 1545, 1570, 1572, 1588, 
                    1594, 1599, 1611, 1637, 1692, 1696, 1727, 1739, 1763, 1821, 1826, 1844, 
                    1864, 1897, 1970, 1980, 2030, 2032, 2044, 2048, 2094, 2101, 2130, 2151, 
                    2164, 2192, 2214, 2254, 2269, 2274, 2278, 2282, 2303, 2330, 2339, 2352, 
                    2356, 2359, 2373, 2391, 2399, 2438, 2443, 2455, 2459, 2476, 2496, 2502, 
                    2519, 2554, 2658, 2700, 2711, 2738, 2797, 2798, 2804, 2829, 2835, 2844, 
                    2846, 2916, 2930, 2935, 2937, 2962, 2974, 2981, 2994, 3004, 3005, 3025, 
                    3028, 3032, 3050, 3066, 3070, 3074, 3078, 3079, 3087, 3125, 3134, 3182, 
                    3197, 3204, 3206, 3216, 3257, 3273, 3299, 3327, 3331, 3341, 3366, 3385, 
                    3405, 3437, 3439, 3467, 3475, 3484, 3496, 3505, 3513, 3530, 3542, 3578, 
                    3605, 3626, 3633, 3639, 3650, 3674, 3702, 3740, 3766, 3783, 3816, 3817, 
                    3834, 3838, 3868, 3913, 3924, 3942, 3943, 3976, 3979]
    def getBirdFileNames(self):
        return self.BirdFileNames

    def getMissingDataBirdTest(self):
        return self.missingDataBirdTest

if __name__ == '__main__':
    testthing = Properties()
    print(testthing.getMissingDataBirdTest())
    print(testthing.getBirdFileNames()[3])
