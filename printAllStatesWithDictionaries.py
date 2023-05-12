#dictionary with all states:
allStates = {1: 'Connecticut', 2: 'Maine', 3: 'Massachusetts', 4: 'New Hampshire', 5: 'Rhode Island', 6: 'Vermont', 7: 'Delaware', 8: 'District of Columbia', 9: 'Maryland', 10: 'New Jersey', 11: 'New York', 12: 'Pennsylvania', 13: 'Illinois', 14: 'Indiana', 15: 'Iowa', 16: 'Michigan', 17: 'Minnesota', 18: 'Missouri', 19: 'Ohio', 20: 'Wisconsin', 21: 'Kansas', 22: 'Nebraska', 23: 'North Dakota', 24: 'Oklahoma', 25: 'South Dakota', 26: 'Colorado', 27: 'Idaho', 28: 'Montana', 29: 'Utah', 30: 'Wyoming', 31: 'California', 32: 'Oregon', 33: 'Washington', 34: 'Arizona', 35: 'Nevada', 36: 'New Mexico', 37: 'Texas', 38: 'Alabama', 39: 'Arkansas', 40: 'Florida', 41: 'Georgia', 42: 'Kentucky', 43: 'Louisiana', 44: 'Mississippi', 45: 'North Carolina', 46: 'South Carolina', 47: 'Tennessee', 48: 'Virginia', 49: 'West Virginia', 50: 'Alaska', 51: 'Hawaii'}
#dictionary w abbreviations:
allStateAbbrs = {1: 'CT', 2: 'ME', 3: 'MA', 4: 'NH', 5: 'RI', 6: 'VT', 7: 'DE', 8: 'DC', 9: 'MD', 10: 'NJ', 11: 'NY', 12: 'PA', 13: 'IL', 14: 'IN', 15: 'IA', 16: 'MI', 17: 'MN', 18: 'MO', 19: 'OH', 20: 'WI', 21: 'KS', 22: 'NE', 23: 'ND', 24: 'OK', 25: 'SD', 26: 'CO', 27: 'ID', 28: 'MT', 29: 'UT', 30: 'WY', 31: 'CA', 32: 'OR', 33: 'WA', 34: 'AZ', 35: 'NV', 36: 'NM', 37: 'TX', 38: 'AL', 39: 'AR', 40: 'FL', 41: 'GA', 42: 'KY', 43: 'LA', 44: 'MS', 45: 'NC', 46: 'SC', 47: 'TN', 48: 'VA', 49: 'WV', 50: 'AK', 51: 'HI'}

#prints all state names:
def printStateNames():
    #Regions based on map by Legends of America: https://www.legendsofamerica.com/ah-geosum/
    print("New England:") #above MD line
    print("1. Connecticut")
    print("2. Maine")
    print("3. Massachusetts")
    print("4. New Hampshire")
    print("5. Rhode Island")
    print("6. Vermont")

    print("\nMid-Atlantic:") #above MD line
    print("7. Delaware")
    print("8. District of Columbia (DC)")
    print("9. Maryland")
    print("10. New Jersey")
    print("11. New York")
    print("12. Pennsylvania")
    
    print("\nMidwest:")
    print("13. Illinois")
    print("14. Indiana")
    print("15. Iowa")
    print("16. Michigan")
    print("17. Minnesota")
    print("18. Missouri")
    print("19. Ohio")
    print("20. Wisconsin")
    
    print("\nGreat Plains:")
    print("21. Kansas")
    print("22. Nebraska")
    print("23. North Dakota")
    print("24. Oklahoma")
    print("25. South Dakota")
    
    print("\nRocky Mountains:")
    print("26. Colorado")
    print("27. Idaho")
    print("28. Montana")
    print("29. Utah")
    print("30. Wyoming")

    print("\nWest Coast:")
    print("31. California")
    print("32. Oregon")
    print("33. Washington")

    print("\nSouthwest:")
    print("34. Arizona")
    print("35. Nevada")
    print("36. New Mexico")
    print("37. Texas")

    print("\nSoutheast:") #below MD line
    print("38. Alabama")
    print("39. Arkansas")
    print("40. Florida")
    print("41. Georgia")
    print("42. Kentucky")
    print("43. Louisiana")
    print("44. Mississippi")
    print("45. North Carolina")
    print("46. South Carolina")
    print("47. Tennessee")
    print("48. Virginia")
    print("49. West Virginia")

    print("\nOther:")
    print("50. Alaska")
    print("51. Hawaii\n")
