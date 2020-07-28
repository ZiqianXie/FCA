from utils import FormalContext


triangle = {"T1": {'b', 'd'},
            "T2": {'b', 'e'},
            "T3": {'c'},
            "T4": {'a', 'b', 'c'},
            "T5": {'d'},
            "T6": {'b', 'c'},
            "T7": {'e'}}
fc = FormalContext(triangle)
for concept in fc._concept_generation():
    print(concept)

star_alliance = {"Air Canada": {"Latin America", "Europe", "Canada", "Asian Pacific", "Middle East", "Mexico",
                                "Caribbean", "United States"},
                 "Air New Zealand": {"Europe", "Asian Pacific", "United States"},
                 "All Nippon Airways": {"Europe", "Asian Pacific", "United States"},
                 "Ansett Australia": {"Asian Pacific"},
                 "The Austrian Airlines Group": {"Europe", "Canada", "Asian Pacific", "Middle East", "Africa",
                                                 "United States"},
                 "British Midland": {"Europe"},
                 "Lufthansa": {"Latin America", "Europe", "Canada", "Asian Pacific", "Middle East", "Africa", "Mexico",
                               "United States"},
                 "Mexicana": {"Latin America", "Canada", "Mexico", "Caribbean", "United States"},
                 "Singapore Airlines": {"Europe", "Canada", "Asian Pacific", "Middle East", "Africa",
                                           "United States"},
                 "Scandinavian Airlines": {"Latin America", "Europe", "Asian Pacific", "Africa", "United States"},
                 "Thai Airways International": {"Latin America", "Europe", "Asian Pacific", "Caribbean",
                                                "United States"},
                 "United Airlines": {"Latin America", "Europe", "Canada", "Asian Pacific", "Mexico", "Caribbean",
                                     "United States"},
                 "VARIG": {"Latin America", "Europe", "Asian Pacific", "Africa", "Mexico", "United States"}
                 }
fc1 = FormalContext(star_alliance)
fc1.attr_closure({"Latin America", "Canada", "Middle East"})
fc1.attributes = ["Latin America", "Europe", "Canada", "Asian Pacific", "Middle East", "Africa", "Mexico", "Caribbean",
                  "United States"]
fc1._next_closure({"Latin America", "Canada", "Mexico", "Caribbean", "United States"})
len(fc1.concept)
p4 = {1: {'a', 'c', 'f'},
      2: {'b', 'd', 'f'},
      3: {'b', 'c', 'e', 'f'},
      4: {'b', 'c', 'f'},
      5: {'d', 'f'},
      6: {'a', 'b', 'c', 'e', 'f'},
      7: {'b', 'd', 'f'}}
fc2 = FormalContext(p4)
fc2._next_closure({'b', 'd', 'f'})
p5 = {1: {'b', 'c', 'e', 'f'},
      2: {'b', 'c'},
      3: {},
      4: {'e', 'f'},
      5: {'c', 'e', 'f'},
      6: {'b'},
      7: {'c', 'e', 'f'},
      8: {'c', 'd', 'f'},
      9: {'c', 'e', 'f'},
      10: {'b', 'c', 'd', 'e', 'f'}}
fc3 = FormalContext(p5)
fc3.add_unused_attributes(['a'])
len(fc3.concept)