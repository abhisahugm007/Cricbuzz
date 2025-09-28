# import pandas as pd


# matches_list = {
#     "typeMatches": [
#         {
#             "matchType": "International",
#             "seriesMatches": [
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 10587,
#                         "seriesName": "Asia Cup 2025",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 130096,
#                                     "seriesId": 10587,
#                                     "seriesName": "Asia Cup 2025",
#                                     "matchDesc": "10th Match, Group A",
#                                     "matchFormat": "T20",
#                                     "startDate": "1758119400000",
#                                     "endDate": "1758132000000",
#                                     "state": "Complete",
#                                     "status": "Pakistan won by 41 runs",
#                                     "team1": {
#                                         "teamId": 3,
#                                         "teamName": "Pakistan",
#                                         "teamSName": "PAK",
#                                         "imageId": 591986,
#                                     },
#                                     "team2": {
#                                         "teamId": 7,
#                                         "teamName": "United Arab Emirates",
#                                         "teamSName": "UAE",
#                                         "imageId": 172121,
#                                     },
#                                     "venueInfo": {
#                                         "id": 153,
#                                         "ground": "Dubai International Cricket Stadium",
#                                         "city": "Dubai",
#                                         "timezone": "+04:00",
#                                         "latitude": "25.046842",
#                                         "longitude": "55.218969",
#                                     },
#                                     "currBatTeamId": 3,
#                                     "seriesStartDt": "1757289600000",
#                                     "seriesEndDt": "1759104000000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "PAK Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 146,
#                                             "wickets": 9,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 105,
#                                             "wickets": 10,
#                                             "overs": 17.4,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 130113,
#                                     "seriesId": 10587,
#                                     "seriesName": "Asia Cup 2025",
#                                     "matchDesc": "12th Match, Group A",
#                                     "matchFormat": "T20",
#                                     "startDate": "1758292200000",
#                                     "endDate": "1758304800000",
#                                     "state": "Complete",
#                                     "status": "India won by 21 runs",
#                                     "team1": {
#                                         "teamId": 2,
#                                         "teamName": "India",
#                                         "teamSName": "IND",
#                                         "imageId": 719031,
#                                     },
#                                     "team2": {
#                                         "teamId": 304,
#                                         "teamName": "Oman",
#                                         "teamSName": "OMAN",
#                                         "imageId": 172353,
#                                     },
#                                     "venueInfo": {
#                                         "id": 94,
#                                         "ground": "Sheikh Zayed Stadium",
#                                         "city": "Abu Dhabi",
#                                         "timezone": "+04:00",
#                                         "latitude": "24.416138",
#                                         "longitude": "54.453566",
#                                     },
#                                     "currBatTeamId": 2,
#                                     "seriesStartDt": "1757289600000",
#                                     "seriesEndDt": "1759104000000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "Complete",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 188,
#                                             "wickets": 8,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 167,
#                                             "wickets": 4,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 130085,
#                                     "seriesId": 10587,
#                                     "seriesName": "Asia Cup 2025",
#                                     "matchDesc": "9th Match, Group B",
#                                     "matchFormat": "T20",
#                                     "startDate": "1758033000000",
#                                     "endDate": "1758045600000",
#                                     "state": "Complete",
#                                     "status": "Bangladesh won by 8 runs",
#                                     "team1": {
#                                         "teamId": 6,
#                                         "teamName": "Bangladesh",
#                                         "teamSName": "BAN",
#                                         "imageId": 172120,
#                                     },
#                                     "team2": {
#                                         "teamId": 96,
#                                         "teamName": "Afghanistan",
#                                         "teamSName": "AFG",
#                                         "imageId": 172188,
#                                     },
#                                     "venueInfo": {
#                                         "id": 94,
#                                         "ground": "Sheikh Zayed Stadium",
#                                         "city": "Abu Dhabi",
#                                         "timezone": "+04:00",
#                                         "latitude": "24.416138",
#                                         "longitude": "54.453566",
#                                     },
#                                     "currBatTeamId": 6,
#                                     "seriesStartDt": "1757289600000",
#                                     "seriesEndDt": "1759104000000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "BAN Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 154,
#                                             "wickets": 5,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 146,
#                                             "wickets": 10,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 130080,
#                                     "seriesId": 10587,
#                                     "seriesName": "Asia Cup 2025",
#                                     "matchDesc": "8th Match, Group B",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757946600000",
#                                     "endDate": "1757959200000",
#                                     "state": "Complete",
#                                     "status": "Sri Lanka won by 4 wkts",
#                                     "team1": {
#                                         "teamId": 8,
#                                         "teamName": "Hong Kong",
#                                         "teamSName": "HK",
#                                         "imageId": 172122,
#                                     },
#                                     "team2": {
#                                         "teamId": 5,
#                                         "teamName": "Sri Lanka",
#                                         "teamSName": "SL",
#                                         "imageId": 172119,
#                                     },
#                                     "venueInfo": {
#                                         "id": 153,
#                                         "ground": "Dubai International Cricket Stadium",
#                                         "city": "Dubai",
#                                         "timezone": "+04:00",
#                                         "latitude": "25.046842",
#                                         "longitude": "55.218969",
#                                     },
#                                     "currBatTeamId": 5,
#                                     "seriesStartDt": "1757289600000",
#                                     "seriesEndDt": "1759104000000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "SL Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 149,
#                                             "wickets": 4,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 153,
#                                             "wickets": 6,
#                                             "overs": 18.5,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 130102,
#                                     "seriesId": 10587,
#                                     "seriesName": "Asia Cup 2025",
#                                     "matchDesc": "11th Match, Group B",
#                                     "matchFormat": "T20",
#                                     "startDate": "1758205800000",
#                                     "endDate": "1758218400000",
#                                     "state": "Complete",
#                                     "status": "Sri Lanka won by 6 wkts",
#                                     "team1": {
#                                         "teamId": 96,
#                                         "teamName": "Afghanistan",
#                                         "teamSName": "AFG",
#                                         "imageId": 172188,
#                                     },
#                                     "team2": {
#                                         "teamId": 5,
#                                         "teamName": "Sri Lanka",
#                                         "teamSName": "SL",
#                                         "imageId": 172119,
#                                     },
#                                     "venueInfo": {
#                                         "id": 94,
#                                         "ground": "Sheikh Zayed Stadium",
#                                         "city": "Abu Dhabi",
#                                         "timezone": "+04:00",
#                                         "latitude": "24.416138",
#                                         "longitude": "54.453566",
#                                     },
#                                     "currBatTeamId": 5,
#                                     "seriesStartDt": "1757289600000",
#                                     "seriesEndDt": "1759104000000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "SL Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 169,
#                                             "wickets": 8,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 171,
#                                             "wickets": 4,
#                                             "overs": 18.4,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 130069,
#                                     "seriesId": 10587,
#                                     "seriesName": "Asia Cup 2025",
#                                     "matchDesc": "6th Match, Group A",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757860200000",
#                                     "endDate": "1757872800000",
#                                     "state": "Complete",
#                                     "status": "India won by 7 wkts",
#                                     "team1": {
#                                         "teamId": 3,
#                                         "teamName": "Pakistan",
#                                         "teamSName": "PAK",
#                                         "imageId": 591986,
#                                     },
#                                     "team2": {
#                                         "teamId": 2,
#                                         "teamName": "India",
#                                         "teamSName": "IND",
#                                         "imageId": 719031,
#                                     },
#                                     "venueInfo": {
#                                         "id": 153,
#                                         "ground": "Dubai International Cricket Stadium",
#                                         "city": "Dubai",
#                                         "timezone": "+04:00",
#                                         "latitude": "25.046842",
#                                         "longitude": "55.218969",
#                                     },
#                                     "currBatTeamId": 2,
#                                     "seriesStartDt": "1757289600000",
#                                     "seriesEndDt": "1759104000000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "IND Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 127,
#                                             "wickets": 9,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 131,
#                                             "wickets": 3,
#                                             "overs": 15.5,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 130058,
#                                     "seriesId": 10587,
#                                     "seriesName": "Asia Cup 2025",
#                                     "matchDesc": "5th Match, Group B",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757773800000",
#                                     "endDate": "1757786400000",
#                                     "state": "Complete",
#                                     "status": "Sri Lanka won by 6 wkts",
#                                     "team1": {
#                                         "teamId": 6,
#                                         "teamName": "Bangladesh",
#                                         "teamSName": "BAN",
#                                         "imageId": 172120,
#                                     },
#                                     "team2": {
#                                         "teamId": 5,
#                                         "teamName": "Sri Lanka",
#                                         "teamSName": "SL",
#                                         "imageId": 172119,
#                                     },
#                                     "venueInfo": {
#                                         "id": 94,
#                                         "ground": "Sheikh Zayed Stadium",
#                                         "city": "Abu Dhabi",
#                                         "timezone": "+04:00",
#                                         "latitude": "24.416138",
#                                         "longitude": "54.453566",
#                                     },
#                                     "currBatTeamId": 5,
#                                     "seriesStartDt": "1757289600000",
#                                     "seriesEndDt": "1759104000000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "SL Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 139,
#                                             "wickets": 5,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 140,
#                                             "wickets": 4,
#                                             "overs": 14.4,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 130074,
#                                     "seriesId": 10587,
#                                     "seriesName": "Asia Cup 2025",
#                                     "matchDesc": "7th Match, Group A",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757937600000",
#                                     "endDate": "1757950200000",
#                                     "state": "Complete",
#                                     "status": "United Arab Emirates won by 42 runs",
#                                     "team1": {
#                                         "teamId": 7,
#                                         "teamName": "United Arab Emirates",
#                                         "teamSName": "UAE",
#                                         "imageId": 172121,
#                                     },
#                                     "team2": {
#                                         "teamId": 304,
#                                         "teamName": "Oman",
#                                         "teamSName": "OMAN",
#                                         "imageId": 172353,
#                                     },
#                                     "venueInfo": {
#                                         "id": 94,
#                                         "ground": "Sheikh Zayed Stadium",
#                                         "city": "Abu Dhabi",
#                                         "timezone": "+04:00",
#                                         "latitude": "24.416138",
#                                         "longitude": "54.453566",
#                                     },
#                                     "currBatTeamId": 7,
#                                     "seriesStartDt": "1757289600000",
#                                     "seriesEndDt": "1759104000000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "UAE Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 172,
#                                             "wickets": 5,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 130,
#                                             "wickets": 10,
#                                             "overs": 18.4,
#                                         }
#                                     },
#                                 },
#                             },
#                         ],
#                     }
#                 },
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 8802,
#                         "seriesName": "England tour of Ireland, 2025",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 105850,
#                                     "seriesId": 8802,
#                                     "seriesName": "England tour of Ireland, 2025",
#                                     "matchDesc": "2nd T20I",
#                                     "matchFormat": "T20",
#                                     "startDate": "1758285000000",
#                                     "endDate": "1758297600000",
#                                     "state": "Abandon",
#                                     "status": "Match abandoned due to rain (no toss)",
#                                     "team1": {
#                                         "teamId": 27,
#                                         "teamName": "Ireland",
#                                         "teamSName": "IRE",
#                                         "imageId": 495001,
#                                     },
#                                     "team2": {
#                                         "teamId": 9,
#                                         "teamName": "England",
#                                         "teamSName": "ENG",
#                                         "imageId": 172123,
#                                     },
#                                     "venueInfo": {
#                                         "id": 370,
#                                         "ground": "The Village",
#                                         "city": "Dublin",
#                                         "timezone": "+01:00",
#                                         "latitude": "53.32568",
#                                         "longitude": "-6.261829",
#                                     },
#                                     "seriesStartDt": "1757980800000",
#                                     "seriesEndDt": "1758499200000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "Abandon",
#                                 }
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 105844,
#                                     "seriesId": 8802,
#                                     "seriesName": "England tour of Ireland, 2025",
#                                     "matchDesc": "1st T20I",
#                                     "matchFormat": "T20",
#                                     "startDate": "1758112200000",
#                                     "endDate": "1758124800000",
#                                     "state": "Complete",
#                                     "status": "England won by 4 wkts",
#                                     "team1": {
#                                         "teamId": 27,
#                                         "teamName": "Ireland",
#                                         "teamSName": "IRE",
#                                         "imageId": 495001,
#                                     },
#                                     "team2": {
#                                         "teamId": 9,
#                                         "teamName": "England",
#                                         "teamSName": "ENG",
#                                         "imageId": 172123,
#                                     },
#                                     "venueInfo": {
#                                         "id": 370,
#                                         "ground": "The Village",
#                                         "city": "Dublin",
#                                         "timezone": "+01:00",
#                                         "latitude": "53.32568",
#                                         "longitude": "-6.261829",
#                                     },
#                                     "currBatTeamId": 9,
#                                     "seriesStartDt": "1757980800000",
#                                     "seriesEndDt": "1758499200000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "ENG Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 196,
#                                             "wickets": 3,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 197,
#                                             "wickets": 6,
#                                             "overs": 17.4,
#                                         }
#                                     },
#                                 },
#                             },
#                         ],
#                     }
#                 },
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 10917,
#                         "seriesName": "Mozambique tour of Eswatini 2025",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 134683,
#                                     "seriesId": 10917,
#                                     "seriesName": "Mozambique tour of Eswatini 2025",
#                                     "matchDesc": "3rd T20I",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757748600000",
#                                     "endDate": "1757761200000",
#                                     "state": "Complete",
#                                     "status": "Eswatini won by 74 runs",
#                                     "team1": {
#                                         "teamId": 1284,
#                                         "teamName": "Eswatini",
#                                         "teamSName": "SWT",
#                                         "imageId": 248525,
#                                     },
#                                     "team2": {
#                                         "teamId": 551,
#                                         "teamName": "Mozambique",
#                                         "teamSName": "MOZ",
#                                         "imageId": 172603,
#                                     },
#                                     "venueInfo": {
#                                         "id": 1877,
#                                         "ground": "Malkerns Country Club oval",
#                                         "city": "Malkerns",
#                                         "timezone": "+02:00",
#                                         "latitude": "-26.52192",
#                                         "longitude": "31.19320",
#                                     },
#                                     "currBatTeamId": 1284,
#                                     "seriesStartDt": "1757548800000",
#                                     "seriesEndDt": "1757894400000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "SWT Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 182,
#                                             "wickets": 6,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 108,
#                                             "wickets": 10,
#                                             "overs": 16.5,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 134705,
#                                     "seriesId": 10917,
#                                     "seriesName": "Mozambique tour of Eswatini 2025",
#                                     "matchDesc": "5th T20I",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757847600000",
#                                     "endDate": "1757860200000",
#                                     "state": "Complete",
#                                     "status": "No result due to rain",
#                                     "team1": {
#                                         "teamId": 1284,
#                                         "teamName": "Eswatini",
#                                         "teamSName": "SWT",
#                                         "imageId": 248525,
#                                     },
#                                     "team2": {
#                                         "teamId": 551,
#                                         "teamName": "Mozambique",
#                                         "teamSName": "MOZ",
#                                         "imageId": 172603,
#                                     },
#                                     "venueInfo": {
#                                         "id": 1877,
#                                         "ground": "Malkerns Country Club oval",
#                                         "city": "Malkerns",
#                                         "timezone": "+02:00",
#                                         "latitude": "-26.52192",
#                                         "longitude": "31.19320",
#                                     },
#                                     "seriesStartDt": "1757548800000",
#                                     "seriesEndDt": "1757894400000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "Complete",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 27,
#                                             "wickets": 3,
#                                             "overs": 4.3,
#                                         }
#                                     }
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 134694,
#                                     "seriesId": 10917,
#                                     "seriesName": "Mozambique tour of Eswatini 2025",
#                                     "matchDesc": "4th T20I",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757763000000",
#                                     "endDate": "1757775600000",
#                                     "state": "Complete",
#                                     "status": "Match tied (Eswatini won the Super Over)  ",
#                                     "team1": {
#                                         "teamId": 1284,
#                                         "teamName": "Eswatini",
#                                         "teamSName": "SWT",
#                                         "imageId": 248525,
#                                     },
#                                     "team2": {
#                                         "teamId": 551,
#                                         "teamName": "Mozambique",
#                                         "teamSName": "MOZ",
#                                         "imageId": 172603,
#                                     },
#                                     "venueInfo": {
#                                         "id": 1877,
#                                         "ground": "Malkerns Country Club oval",
#                                         "city": "Malkerns",
#                                         "timezone": "+02:00",
#                                         "latitude": "-26.52192",
#                                         "longitude": "31.19320",
#                                     },
#                                     "seriesStartDt": "1757548800000",
#                                     "seriesEndDt": "1757894400000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "Complete",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 222,
#                                             "wickets": 4,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 222,
#                                             "wickets": 4,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                 },
#                             },
#                         ],
#                     }
#                 },
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 10928,
#                         "seriesName": "Namibia tour of Zimbabwe 2025",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 134733,
#                                     "seriesId": 10928,
#                                     "seriesName": "Namibia tour of Zimbabwe 2025",
#                                     "matchDesc": "3rd T20I",
#                                     "matchFormat": "T20",
#                                     "startDate": "1758195000000",
#                                     "endDate": "1758207600000",
#                                     "state": "Complete",
#                                     "status": "Namibia won by 28 runs",
#                                     "team1": {
#                                         "teamId": 161,
#                                         "teamName": "Namibia",
#                                         "teamSName": "NAM",
#                                         "imageId": 172229,
#                                     },
#                                     "team2": {
#                                         "teamId": 12,
#                                         "teamName": "Zimbabwe",
#                                         "teamSName": "ZIM",
#                                         "imageId": 172127,
#                                     },
#                                     "venueInfo": {
#                                         "id": 70,
#                                         "ground": "Queens Sports Club",
#                                         "city": "Bulawayo",
#                                         "timezone": "+02:00",
#                                         "latitude": "-20.145151",
#                                         "longitude": "28.588901",
#                                     },
#                                     "currBatTeamId": 161,
#                                     "seriesStartDt": "1757808000000",
#                                     "seriesEndDt": "1758240000000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "NAM Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 204,
#                                             "wickets": 7,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 176,
#                                             "wickets": 10,
#                                             "overs": 19.5,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 134722,
#                                     "seriesId": 10928,
#                                     "seriesName": "Namibia tour of Zimbabwe 2025",
#                                     "matchDesc": " 2nd T20I",
#                                     "matchFormat": "T20",
#                                     "startDate": "1758022200000",
#                                     "endDate": "1758034800000",
#                                     "state": "Complete",
#                                     "status": "Zimbabwe won by 5 wkts",
#                                     "team1": {
#                                         "teamId": 161,
#                                         "teamName": "Namibia",
#                                         "teamSName": "NAM",
#                                         "imageId": 172229,
#                                     },
#                                     "team2": {
#                                         "teamId": 12,
#                                         "teamName": "Zimbabwe",
#                                         "teamSName": "ZIM",
#                                         "imageId": 172127,
#                                     },
#                                     "venueInfo": {
#                                         "id": 70,
#                                         "ground": "Queens Sports Club",
#                                         "city": "Bulawayo",
#                                         "timezone": "+02:00",
#                                         "latitude": "-20.145151",
#                                         "longitude": "28.588901",
#                                     },
#                                     "currBatTeamId": 12,
#                                     "seriesStartDt": "1757808000000",
#                                     "seriesEndDt": "1758240000000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "ZIM Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 169,
#                                             "wickets": 6,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 170,
#                                             "wickets": 5,
#                                             "overs": 18.1,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 134711,
#                                     "seriesId": 10928,
#                                     "seriesName": "Namibia tour of Zimbabwe 2025",
#                                     "matchDesc": "1st T20I",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757921400000",
#                                     "endDate": "1757934000000",
#                                     "state": "Complete",
#                                     "status": "Zimbabwe won by 33 runs",
#                                     "team1": {
#                                         "teamId": 12,
#                                         "teamName": "Zimbabwe",
#                                         "teamSName": "ZIM",
#                                         "imageId": 172127,
#                                     },
#                                     "team2": {
#                                         "teamId": 161,
#                                         "teamName": "Namibia",
#                                         "teamSName": "NAM",
#                                         "imageId": 172229,
#                                     },
#                                     "venueInfo": {
#                                         "id": 70,
#                                         "ground": "Queens Sports Club",
#                                         "city": "Bulawayo",
#                                         "timezone": "+02:00",
#                                         "latitude": "-20.145151",
#                                         "longitude": "28.588901",
#                                     },
#                                     "currBatTeamId": 12,
#                                     "seriesStartDt": "1757808000000",
#                                     "seriesEndDt": "1758240000000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "ZIM Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 211,
#                                             "wickets": 3,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 178,
#                                             "wickets": 7,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                 },
#                             },
#                         ],
#                     }
#                 },
#                 {
#                     "ad": {
#                         "name": "native_matches",
#                         "layout": "native_large",
#                         "position": 4,
#                     }
#                 },
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 8788,
#                         "seriesName": "South Africa tour of England, 2025",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 105812,
#                                     "seriesId": 8788,
#                                     "seriesName": "South Africa tour of England, 2025",
#                                     "matchDesc": "3rd T20I",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757856600000",
#                                     "endDate": "1757869200000",
#                                     "state": "Abandon",
#                                     "status": "Match abandoned due to rain (no toss)",
#                                     "team1": {
#                                         "teamId": 9,
#                                         "teamName": "England",
#                                         "teamSName": "ENG",
#                                         "imageId": 172123,
#                                     },
#                                     "team2": {
#                                         "teamId": 11,
#                                         "teamName": "South Africa",
#                                         "teamSName": "RSA",
#                                         "imageId": 172126,
#                                     },
#                                     "venueInfo": {
#                                         "id": 18,
#                                         "ground": "Trent Bridge",
#                                         "city": "Nottingham",
#                                         "timezone": "+01:00",
#                                         "latitude": "52.936884",
#                                         "longitude": "-1.132230",
#                                     },
#                                     "seriesStartDt": "1756684800000",
#                                     "seriesEndDt": "1757894400000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "Abandon",
#                                 }
#                             }
#                         ],
#                     }
#                 },
#             ],
#         },
#         {
#             "matchType": "League",
#             "seriesMatches": [
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 9575,
#                         "seriesName": "Caribbean Premier League 2025",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 116822,
#                                     "seriesId": 9575,
#                                     "seriesName": "Caribbean Premier League 2025",
#                                     "matchDesc": "Qualifier 2",
#                                     "matchFormat": "T20",
#                                     "startDate": "1758326400000",
#                                     "endDate": "1758339000000",
#                                     "state": "Complete",
#                                     "status": "Trinbago Knight Riders won by 56 runs",
#                                     "team1": {
#                                         "teamId": 271,
#                                         "teamName": "Trinbago Knight Riders",
#                                         "teamSName": "TKR",
#                                         "imageId": 172325,
#                                     },
#                                     "team2": {
#                                         "teamId": 263,
#                                         "teamName": "Saint Lucia Kings",
#                                         "teamSName": "SLK",
#                                         "imageId": 172316,
#                                     },
#                                     "venueInfo": {
#                                         "id": 110,
#                                         "ground": "Providence Stadium",
#                                         "city": "Guyana",
#                                         "timezone": "-04:00",
#                                         "latitude": "41.823872",
#                                         "longitude": "-71.411987",
#                                     },
#                                     "currBatTeamId": 271,
#                                     "seriesStartDt": "1755043200000",
#                                     "seriesEndDt": "1758499200000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "Complete",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 194,
#                                             "wickets": 4,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 138,
#                                             "wickets": 8,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 116813,
#                                     "seriesId": 9575,
#                                     "seriesName": "Caribbean Premier League 2025",
#                                     "matchDesc": "Eliminator",
#                                     "matchFormat": "T20",
#                                     "startDate": "1758067200000",
#                                     "endDate": "1758079800000",
#                                     "state": "Complete",
#                                     "status": "Trinbago Knight Riders won by 9 wkts",
#                                     "team1": {
#                                         "teamId": 1978,
#                                         "teamName": "Antigua and Barbuda Falcons",
#                                         "teamSName": "ABF",
#                                         "imageId": 507236,
#                                     },
#                                     "team2": {
#                                         "teamId": 271,
#                                         "teamName": "Trinbago Knight Riders",
#                                         "teamSName": "TKR",
#                                         "imageId": 172325,
#                                     },
#                                     "venueInfo": {
#                                         "id": 110,
#                                         "ground": "Providence Stadium",
#                                         "city": "Guyana",
#                                         "timezone": "-04:00",
#                                         "latitude": "41.823872",
#                                         "longitude": "-71.411987",
#                                     },
#                                     "currBatTeamId": 271,
#                                     "seriesStartDt": "1755043200000",
#                                     "seriesEndDt": "1758499200000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "TKR Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 166,
#                                             "wickets": 8,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 168,
#                                             "wickets": 1,
#                                             "overs": 17.3,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 116819,
#                                     "seriesId": 9575,
#                                     "seriesName": "Caribbean Premier League 2025",
#                                     "matchDesc": "Qualifier 1",
#                                     "matchFormat": "T20",
#                                     "startDate": "1758153600000",
#                                     "endDate": "1758166200000",
#                                     "state": "Complete",
#                                     "status": "Guyana Amazon Warriors won by 14 runs",
#                                     "team1": {
#                                         "teamId": 159,
#                                         "teamName": "Guyana Amazon Warriors",
#                                         "teamSName": "GAW",
#                                         "imageId": 172227,
#                                     },
#                                     "team2": {
#                                         "teamId": 263,
#                                         "teamName": "Saint Lucia Kings",
#                                         "teamSName": "SLK",
#                                         "imageId": 172316,
#                                     },
#                                     "venueInfo": {
#                                         "id": 110,
#                                         "ground": "Providence Stadium",
#                                         "city": "Guyana",
#                                         "timezone": "-04:00",
#                                         "latitude": "41.823872",
#                                         "longitude": "-71.411987",
#                                     },
#                                     "currBatTeamId": 159,
#                                     "seriesStartDt": "1755043200000",
#                                     "seriesEndDt": "1758499200000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "GAW Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 157,
#                                             "wickets": 10,
#                                             "overs": 19.5,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 143,
#                                             "wickets": 10,
#                                             "overs": 19.1,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 116810,
#                                     "seriesId": 9575,
#                                     "seriesName": "Caribbean Premier League 2025",
#                                     "matchDesc": "30th Match",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757890800000",
#                                     "endDate": "1757903400000",
#                                     "state": "Complete",
#                                     "status": "Guyana Amazon Warriors won by 64 runs",
#                                     "team1": {
#                                         "teamId": 159,
#                                         "teamName": "Guyana Amazon Warriors",
#                                         "teamSName": "GAW",
#                                         "imageId": 172227,
#                                     },
#                                     "team2": {
#                                         "teamId": 262,
#                                         "teamName": "Barbados Royals",
#                                         "teamSName": "BR",
#                                         "imageId": 210485,
#                                     },
#                                     "venueInfo": {
#                                         "id": 110,
#                                         "ground": "Providence Stadium",
#                                         "city": "Guyana",
#                                         "timezone": "-04:00",
#                                         "latitude": "41.823872",
#                                         "longitude": "-71.411987",
#                                     },
#                                     "currBatTeamId": 159,
#                                     "seriesStartDt": "1755043200000",
#                                     "seriesEndDt": "1758499200000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "GAW Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 189,
#                                             "wickets": 6,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 125,
#                                             "wickets": 10,
#                                             "overs": 18.2,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 116801,
#                                     "seriesId": 9575,
#                                     "seriesName": "Caribbean Premier League 2025",
#                                     "matchDesc": "29th Match",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757775600000",
#                                     "endDate": "1757788200000",
#                                     "state": "Complete",
#                                     "status": "Guyana Amazon Warriors won by 2 wkts",
#                                     "team1": {
#                                         "teamId": 263,
#                                         "teamName": "Saint Lucia Kings",
#                                         "teamSName": "SLK",
#                                         "imageId": 172316,
#                                     },
#                                     "team2": {
#                                         "teamId": 159,
#                                         "teamName": "Guyana Amazon Warriors",
#                                         "teamSName": "GAW",
#                                         "imageId": 172227,
#                                     },
#                                     "venueInfo": {
#                                         "id": 110,
#                                         "ground": "Providence Stadium",
#                                         "city": "Guyana",
#                                         "timezone": "-04:00",
#                                         "latitude": "41.823872",
#                                         "longitude": "-71.411987",
#                                     },
#                                     "currBatTeamId": 159,
#                                     "seriesStartDt": "1755043200000",
#                                     "seriesEndDt": "1758499200000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "GAW Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 185,
#                                             "wickets": 4,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 188,
#                                             "wickets": 8,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                 },
#                             },
#                         ],
#                     }
#                 },
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 9257,
#                         "seriesName": "T20 Blast 2025",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 111101,
#                                     "seriesId": 9257,
#                                     "seriesName": "T20 Blast 2025",
#                                     "matchDesc": "Final",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757785500000",
#                                     "endDate": "1757798100000",
#                                     "state": "Complete",
#                                     "status": "Somerset won by 6 wkts",
#                                     "team1": {
#                                         "teamId": 153,
#                                         "teamName": "Hampshire",
#                                         "teamSName": "HAM",
#                                         "imageId": 172220,
#                                     },
#                                     "team2": {
#                                         "teamId": 119,
#                                         "teamName": "Somerset",
#                                         "teamSName": "SOM",
#                                         "imageId": 172199,
#                                     },
#                                     "venueInfo": {
#                                         "id": 20,
#                                         "ground": "Edgbaston",
#                                         "city": "Birmingham",
#                                         "timezone": "+01:00",
#                                         "latitude": "52.455774",
#                                         "longitude": "-1.902624",
#                                     },
#                                     "currBatTeamId": 119,
#                                     "seriesStartDt": "1748390400000",
#                                     "seriesEndDt": "1757808000000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "SOM Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 194,
#                                             "wickets": 6,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 195,
#                                             "wickets": 4,
#                                             "overs": 18.6,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 111085,
#                                     "seriesId": 9257,
#                                     "seriesName": "T20 Blast 2025",
#                                     "matchDesc": "1st Semi-Final",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757757600000",
#                                     "endDate": "1757770200000",
#                                     "state": "Complete",
#                                     "status": "Somerset won by 23 runs",
#                                     "team1": {
#                                         "teamId": 119,
#                                         "teamName": "Somerset",
#                                         "teamSName": "SOM",
#                                         "imageId": 172199,
#                                     },
#                                     "team2": {
#                                         "teamId": 143,
#                                         "teamName": "Lancashire",
#                                         "teamSName": "LANCS",
#                                         "imageId": 172210,
#                                     },
#                                     "venueInfo": {
#                                         "id": 20,
#                                         "ground": "Edgbaston",
#                                         "city": "Birmingham",
#                                         "timezone": "+01:00",
#                                         "latitude": "52.455774",
#                                         "longitude": "-1.902624",
#                                     },
#                                     "currBatTeamId": 119,
#                                     "seriesStartDt": "1748390400000",
#                                     "seriesEndDt": "1757808000000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "SOM Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 182,
#                                             "wickets": 7,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 159,
#                                             "wickets": 10,
#                                             "overs": 19.5,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 111093,
#                                     "seriesId": 9257,
#                                     "seriesName": "T20 Blast 2025",
#                                     "matchDesc": "2nd Semi-Final",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757770200000",
#                                     "endDate": "1757782800000",
#                                     "state": "Complete",
#                                     "status": "Hampshire won by 6 wkts (DLS method)",
#                                     "team1": {
#                                         "teamId": 142,
#                                         "teamName": "Northamptonshire",
#                                         "teamSName": "NHNTS",
#                                         "imageId": 172209,
#                                     },
#                                     "team2": {
#                                         "teamId": 153,
#                                         "teamName": "Hampshire",
#                                         "teamSName": "HAM",
#                                         "imageId": 172220,
#                                     },
#                                     "venueInfo": {
#                                         "id": 20,
#                                         "ground": "Edgbaston",
#                                         "city": "Birmingham",
#                                         "timezone": "+01:00",
#                                         "latitude": "52.455774",
#                                         "longitude": "-1.902624",
#                                     },
#                                     "currBatTeamId": 153,
#                                     "seriesStartDt": "1748390400000",
#                                     "seriesEndDt": "1757808000000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "HAM Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 158,
#                                             "wickets": 7,
#                                             "overs": 17.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 155,
#                                             "wickets": 4,
#                                             "overs": 15.4,
#                                         }
#                                     },
#                                 },
#                             },
#                         ],
#                     }
#                 },
#             ],
#         },
#         {
#             "matchType": "Domestic",
#             "seriesMatches": [
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 10311,
#                         "seriesName": "Duleep Trophy 2025",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 123688,
#                                     "seriesId": 10311,
#                                     "seriesName": "Duleep Trophy 2025",
#                                     "matchDesc": "Final",
#                                     "matchFormat": "TEST",
#                                     "startDate": "1757563200000",
#                                     "endDate": "1757934000000",
#                                     "state": "Complete",
#                                     "status": "Central Zone won by 6 wkts",
#                                     "team1": {
#                                         "teamId": 236,
#                                         "teamName": "South Zone",
#                                         "teamSName": "SZONE",
#                                         "imageId": 172289,
#                                     },
#                                     "team2": {
#                                         "teamId": 237,
#                                         "teamName": "Central Zone",
#                                         "teamSName": "CZONE",
#                                         "imageId": 172290,
#                                     },
#                                     "venueInfo": {
#                                         "id": 1438087,
#                                         "ground": "BCCI Centre of Excellence Ground",
#                                         "city": "Bengaluru",
#                                         "timezone": "+05:30",
#                                         "latitude": "12.978853",
#                                         "longitude": "77.599533",
#                                     },
#                                     "currBatTeamId": 237,
#                                     "seriesStartDt": "1756252800000",
#                                     "seriesEndDt": "1757980800000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "CZONE Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 149,
#                                             "wickets": 10,
#                                             "overs": 62.6,
#                                         },
#                                         "inngs2": {
#                                             "inningsId": 3,
#                                             "runs": 426,
#                                             "wickets": 10,
#                                             "overs": 120.6,
#                                         },
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 511,
#                                             "wickets": 10,
#                                             "overs": 145.1,
#                                         },
#                                         "inngs2": {
#                                             "inningsId": 4,
#                                             "runs": 66,
#                                             "wickets": 4,
#                                             "overs": 20.3,
#                                         },
#                                     },
#                                 },
#                             }
#                         ],
#                     }
#                 },
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 10829,
#                         "seriesName": "Australia Domestic One-Day Cup 2025-26",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 133468,
#                                     "seriesId": 10829,
#                                     "seriesName": "Australia Domestic One-Day Cup 2025-26",
#                                     "matchDesc": "3rd Match",
#                                     "matchFormat": "ODI",
#                                     "startDate": "1758254400000",
#                                     "endDate": "1758283200000",
#                                     "state": "Complete",
#                                     "status": "Tasmania won by 109 runs",
#                                     "team1": {
#                                         "teamId": 166,
#                                         "teamName": "Tasmania",
#                                         "teamSName": "TAS",
#                                         "imageId": 172235,
#                                     },
#                                     "team2": {
#                                         "teamId": 52,
#                                         "teamName": "Victoria",
#                                         "teamSName": "VIC",
#                                         "imageId": 172153,
#                                     },
#                                     "venueInfo": {
#                                         "id": 300,
#                                         "ground": "Allan Border Field",
#                                         "city": "Brisbane",
#                                         "timezone": "+10:00",
#                                         "latitude": "-27.435145",
#                                         "longitude": "153.046143",
#                                     },
#                                     "currBatTeamId": 166,
#                                     "seriesStartDt": "1757894400000",
#                                     "seriesEndDt": "1772323200000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "TAS Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 381,
#                                             "wickets": 10,
#                                             "overs": 49.3,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 272,
#                                             "wickets": 10,
#                                             "overs": 40.1,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 133462,
#                                     "seriesId": 10829,
#                                     "seriesName": "Australia Domestic One-Day Cup 2025-26",
#                                     "matchDesc": "2nd Match",
#                                     "matchFormat": "ODI",
#                                     "startDate": "1758065400000",
#                                     "endDate": "1758094200000",
#                                     "state": "Complete",
#                                     "status": "Queensland won by 55 runs",
#                                     "team1": {
#                                         "teamId": 164,
#                                         "teamName": "Queensland",
#                                         "teamSName": "QL",
#                                         "imageId": 172233,
#                                     },
#                                     "team2": {
#                                         "teamId": 52,
#                                         "teamName": "Victoria",
#                                         "teamSName": "VIC",
#                                         "imageId": 172153,
#                                     },
#                                     "venueInfo": {
#                                         "id": 300,
#                                         "ground": "Allan Border Field",
#                                         "city": "Brisbane",
#                                         "timezone": "+10:00",
#                                         "latitude": "-27.435145",
#                                         "longitude": "153.046143",
#                                     },
#                                     "currBatTeamId": 164,
#                                     "seriesStartDt": "1757894400000",
#                                     "seriesEndDt": "1772323200000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "QL Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 310,
#                                             "wickets": 5,
#                                             "overs": 49.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 255,
#                                             "wickets": 10,
#                                             "overs": 46.2,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 133451,
#                                     "seriesId": 10829,
#                                     "seriesName": "Australia Domestic One-Day Cup 2025-26",
#                                     "matchDesc": "1st Match",
#                                     "matchFormat": "ODI",
#                                     "startDate": "1757979000000",
#                                     "endDate": "1758007800000",
#                                     "state": "Complete",
#                                     "status": "Tasmania won by 2 wkts",
#                                     "team1": {
#                                         "teamId": 104,
#                                         "teamName": "New South Wales",
#                                         "teamSName": "NSW",
#                                         "imageId": 172196,
#                                     },
#                                     "team2": {
#                                         "teamId": 166,
#                                         "teamName": "Tasmania",
#                                         "teamSName": "TAS",
#                                         "imageId": 172235,
#                                     },
#                                     "venueInfo": {
#                                         "id": 1727,
#                                         "ground": "Cricket Central",
#                                         "city": "Sydney",
#                                         "timezone": "+11:00",
#                                         "latitude": "-33.82595",
#                                         "longitude": "151.05187",
#                                     },
#                                     "currBatTeamId": 166,
#                                     "seriesStartDt": "1757894400000",
#                                     "seriesEndDt": "1772323200000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "TAS Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 224,
#                                             "wickets": 10,
#                                             "overs": 49.4,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 225,
#                                             "wickets": 8,
#                                             "overs": 49.2,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 133479,
#                                     "seriesId": 10829,
#                                     "seriesName": "Australia Domestic One-Day Cup 2025-26",
#                                     "matchDesc": "4th Match",
#                                     "matchFormat": "ODI",
#                                     "startDate": "1758324600000",
#                                     "endDate": "1758353400000",
#                                     "state": "Complete",
#                                     "status": "New South Wales won by 131 runs",
#                                     "team1": {
#                                         "teamId": 104,
#                                         "teamName": "New South Wales",
#                                         "teamSName": "NSW",
#                                         "imageId": 172196,
#                                     },
#                                     "team2": {
#                                         "teamId": 158,
#                                         "teamName": "South Australia",
#                                         "teamSName": "SAUS",
#                                         "imageId": 172225,
#                                     },
#                                     "venueInfo": {
#                                         "id": 1727,
#                                         "ground": "Cricket Central",
#                                         "city": "Sydney",
#                                         "timezone": "+11:00",
#                                         "latitude": "-33.82595",
#                                         "longitude": "151.05187",
#                                     },
#                                     "currBatTeamId": 104,
#                                     "seriesStartDt": "1757894400000",
#                                     "seriesEndDt": "1772323200000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "NSW Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 288,
#                                             "wickets": 7,
#                                             "overs": 49.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 157,
#                                             "wickets": 10,
#                                             "overs": 36.3,
#                                         }
#                                     },
#                                 },
#                             },
#                         ],
#                     }
#                 },
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 9935,
#                         "seriesName": "Australia A tour of India, 2025",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 119843,
#                                     "seriesId": 9935,
#                                     "seriesName": "Australia A tour of India, 2025",
#                                     "matchDesc": "1st Unofficial Test",
#                                     "matchFormat": "TEST",
#                                     "startDate": "1757995200000",
#                                     "endDate": "1758279600000",
#                                     "state": "Complete",
#                                     "status": "Match drawn",
#                                     "team1": {
#                                         "teamId": 79,
#                                         "teamName": "Australia A",
#                                         "teamSName": "AUSA",
#                                         "imageId": 172173,
#                                     },
#                                     "team2": {
#                                         "teamId": 78,
#                                         "teamName": "India A",
#                                         "teamSName": "INDA",
#                                         "imageId": 693099,
#                                     },
#                                     "venueInfo": {
#                                         "id": 485,
#                                         "ground": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium",
#                                         "city": "Lucknow",
#                                         "timezone": "+05:30",
#                                         "latitude": "26.846694",
#                                         "longitude": "80.946166",
#                                     },
#                                     "seriesStartDt": "1757894400000",
#                                     "seriesEndDt": "1759708800000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "Complete",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 532,
#                                             "wickets": 6,
#                                             "overs": 98,
#                                         },
#                                         "inngs2": {
#                                             "inningsId": 3,
#                                             "runs": 56,
#                                             "overs": 16,
#                                         },
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 531,
#                                             "wickets": 7,
#                                             "overs": 141.1,
#                                         }
#                                     },
#                                 },
#                             }
#                         ],
#                     }
#                 },
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 9360,
#                         "seriesName": "County Championship Division One 2025",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 113235,
#                                     "seriesId": 9360,
#                                     "seriesName": "County Championship Division One 2025",
#                                     "matchDesc": "63rd Match",
#                                     "matchFormat": "TEST",
#                                     "startDate": "1757928600000",
#                                     "endDate": "1758213000000",
#                                     "state": "Complete",
#                                     "status": "Match drawn",
#                                     "team1": {
#                                         "teamId": 146,
#                                         "teamName": "Yorkshire",
#                                         "teamSName": "YORKS",
#                                         "imageId": 172213,
#                                     },
#                                     "team2": {
#                                         "teamId": 41,
#                                         "teamName": "Sussex",
#                                         "teamSName": "SUS",
#                                         "imageId": 172148,
#                                     },
#                                     "venueInfo": {
#                                         "id": 292,
#                                         "ground": "County Ground",
#                                         "city": "Hove",
#                                         "timezone": "+01:00",
#                                         "latitude": "50.830995",
#                                         "longitude": "-0.163522",
#                                     },
#                                     "seriesStartDt": "1743638400000",
#                                     "seriesEndDt": "1759017600000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "Complete",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 194,
#                                             "wickets": 10,
#                                             "overs": 64.1,
#                                         },
#                                         "inngs2": {
#                                             "inningsId": 3,
#                                             "runs": 109,
#                                             "wickets": 3,
#                                             "overs": 36.6,
#                                         },
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 250,
#                                             "wickets": 10,
#                                             "overs": 79.2,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 113229,
#                                     "seriesId": 9360,
#                                     "seriesName": "County Championship Division One 2025",
#                                     "matchDesc": "62nd Match",
#                                     "matchFormat": "TEST",
#                                     "startDate": "1757928600000",
#                                     "endDate": "1758213000000",
#                                     "state": "Complete",
#                                     "status": "Match drawn",
#                                     "team1": {
#                                         "teamId": 147,
#                                         "teamName": "Worcestershire",
#                                         "teamSName": "WORCS",
#                                         "imageId": 172214,
#                                     },
#                                     "team2": {
#                                         "teamId": 141,
#                                         "teamName": "Durham",
#                                         "teamSName": "DUR",
#                                         "imageId": 172208,
#                                     },
#                                     "venueInfo": {
#                                         "id": 60,
#                                         "ground": "Riverside Ground",
#                                         "city": "Chester-le-Street",
#                                         "timezone": "+01:00",
#                                         "latitude": "54.849531",
#                                         "longitude": "-1.56103",
#                                     },
#                                     "seriesStartDt": "1743638400000",
#                                     "seriesEndDt": "1759017600000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "Complete",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 591,
#                                             "wickets": 9,
#                                             "overs": 173.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 450,
#                                             "wickets": 6,
#                                             "overs": 86.4,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 113226,
#                                     "seriesId": 9360,
#                                     "seriesName": "County Championship Division One 2025",
#                                     "matchDesc": "61st Match",
#                                     "matchFormat": "TEST",
#                                     "startDate": "1757928600000",
#                                     "endDate": "1758213000000",
#                                     "state": "Complete",
#                                     "status": "Match drawn",
#                                     "team1": {
#                                         "teamId": 152,
#                                         "teamName": "Essex",
#                                         "teamSName": "ESS",
#                                         "imageId": 172219,
#                                     },
#                                     "team2": {
#                                         "teamId": 140,
#                                         "teamName": "Warwickshire",
#                                         "teamSName": "WARKS",
#                                         "imageId": 172207,
#                                     },
#                                     "venueInfo": {
#                                         "id": 20,
#                                         "ground": "Edgbaston",
#                                         "city": "Birmingham",
#                                         "timezone": "+01:00",
#                                         "latitude": "52.455774",
#                                         "longitude": "-1.902624",
#                                     },
#                                     "seriesStartDt": "1743638400000",
#                                     "seriesEndDt": "1759017600000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "Complete",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 325,
#                                             "wickets": 5,
#                                             "overs": 103.6,
#                                         }
#                                     }
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 113253,
#                                     "seriesId": 9360,
#                                     "seriesName": "County Championship Division One 2025",
#                                     "matchDesc": "65th Match",
#                                     "matchFormat": "TEST",
#                                     "startDate": "1757928600000",
#                                     "endDate": "1758213000000",
#                                     "state": "Complete",
#                                     "status": "Match drawn",
#                                     "team1": {
#                                         "teamId": 119,
#                                         "teamName": "Somerset",
#                                         "teamSName": "SOM",
#                                         "imageId": 172199,
#                                     },
#                                     "team2": {
#                                         "teamId": 153,
#                                         "teamName": "Hampshire",
#                                         "teamSName": "HAM",
#                                         "imageId": 172220,
#                                     },
#                                     "venueInfo": {
#                                         "id": 223,
#                                         "ground": "The Cooper Associates County Ground",
#                                         "city": "Taunton",
#                                         "timezone": "+01:00",
#                                         "latitude": "51.018913",
#                                         "longitude": "3.100894",
#                                     },
#                                     "seriesStartDt": "1743638400000",
#                                     "seriesEndDt": "1759017600000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "Complete",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 454,
#                                             "wickets": 8,
#                                             "overs": 102.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 172,
#                                             "wickets": 10,
#                                             "overs": 54.3,
#                                         },
#                                         "inngs2": {
#                                             "inningsId": 3,
#                                             "runs": 201,
#                                             "wickets": 8,
#                                             "overs": 126.5,
#                                         },
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 113244,
#                                     "seriesId": 9360,
#                                     "seriesName": "County Championship Division One 2025",
#                                     "matchDesc": "64th Match",
#                                     "matchFormat": "TEST",
#                                     "startDate": "1757928600000",
#                                     "endDate": "1758213000000",
#                                     "state": "Complete",
#                                     "status": "Nottinghamshire won by 20 runs",
#                                     "team1": {
#                                         "teamId": 139,
#                                         "teamName": "Nottinghamshire",
#                                         "teamSName": "NOTTS",
#                                         "imageId": 172206,
#                                     },
#                                     "team2": {
#                                         "teamId": 148,
#                                         "teamName": "Surrey",
#                                         "teamSName": "SUR",
#                                         "imageId": 172215,
#                                     },
#                                     "venueInfo": {
#                                         "id": 12,
#                                         "ground": "Kennington Oval",
#                                         "city": "London",
#                                         "timezone": "+01:00",
#                                         "latitude": "51.48368",
#                                         "longitude": "-0.114885",
#                                     },
#                                     "currBatTeamId": 139,
#                                     "seriesStartDt": "1743638400000",
#                                     "seriesEndDt": "1759017600000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "NOTTS Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 231,
#                                             "wickets": 10,
#                                             "overs": 77.4,
#                                         },
#                                         "inngs2": {
#                                             "inningsId": 3,
#                                             "runs": 256,
#                                             "wickets": 10,
#                                             "overs": 66.6,
#                                         },
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 173,
#                                             "wickets": 10,
#                                             "overs": 52.2,
#                                         },
#                                         "inngs2": {
#                                             "inningsId": 4,
#                                             "runs": 294,
#                                             "wickets": 10,
#                                             "overs": 71.2,
#                                         },
#                                     },
#                                 },
#                             },
#                         ],
#                     }
#                 },
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 9557,
#                         "seriesName": "New Zealand A tour of South Africa, 2025",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 116498,
#                                     "seriesId": 9557,
#                                     "seriesName": "New Zealand A tour of South Africa, 2025",
#                                     "matchDesc": "2nd Unofficial Test",
#                                     "matchFormat": "TEST",
#                                     "startDate": "1757836800000",
#                                     "endDate": "1758121200000",
#                                     "state": "Complete",
#                                     "status": "Match drawn",
#                                     "team1": {
#                                         "teamId": 80,
#                                         "teamName": "New Zealand A",
#                                         "teamSName": "NZA",
#                                         "imageId": 172174,
#                                     },
#                                     "team2": {
#                                         "teamId": 268,
#                                         "teamName": "South Africa A",
#                                         "teamSName": "RSAA",
#                                         "imageId": 172321,
#                                     },
#                                     "venueInfo": {
#                                         "id": 367,
#                                         "ground": "LC de Villiers Oval",
#                                         "city": "Pretoria",
#                                         "timezone": "+02:00",
#                                         "latitude": "-25.771079",
#                                         "longitude": "28.221849",
#                                     },
#                                     "seriesStartDt": "1756425600000",
#                                     "seriesEndDt": "1758153600000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "Complete",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 482,
#                                             "wickets": 10,
#                                             "overs": 131.6,
#                                         },
#                                         "inngs2": {
#                                             "inningsId": 3,
#                                             "runs": 298,
#                                             "wickets": 4,
#                                             "overs": 66.6,
#                                         },
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 578,
#                                             "wickets": 8,
#                                             "overs": 114.6,
#                                         }
#                                     },
#                                 },
#                             }
#                         ],
#                     }
#                 },
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 9369,
#                         "seriesName": "County Championship Division Two 2025",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 113649,
#                                     "seriesId": 9369,
#                                     "seriesName": "County Championship Division Two 2025",
#                                     "matchDesc": "52nd Match",
#                                     "matchFormat": "TEST",
#                                     "startDate": "1757928600000",
#                                     "endDate": "1758213000000",
#                                     "state": "Complete",
#                                     "status": "Match drawn",
#                                     "team1": {
#                                         "teamId": 149,
#                                         "teamName": "Glamorgan",
#                                         "teamSName": "GLAM",
#                                         "imageId": 172216,
#                                     },
#                                     "team2": {
#                                         "teamId": 144,
#                                         "teamName": "Derbyshire",
#                                         "teamSName": "DERBY",
#                                         "imageId": 172211,
#                                     },
#                                     "venueInfo": {
#                                         "id": 226,
#                                         "ground": "County Ground",
#                                         "city": "Derby",
#                                         "timezone": "+01:00",
#                                         "latitude": "52.927517",
#                                         "longitude": "-1.461188",
#                                     },
#                                     "seriesStartDt": "1743638400000",
#                                     "seriesEndDt": "1759017600000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "Complete",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 259,
#                                             "wickets": 10,
#                                             "overs": 88.3,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 17,
#                                             "overs": 4.6,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 113631,
#                                     "seriesId": 9369,
#                                     "seriesName": "County Championship Division Two 2025",
#                                     "matchDesc": "49th Match",
#                                     "matchFormat": "TEST",
#                                     "startDate": "1757928600000",
#                                     "endDate": "1758213000000",
#                                     "state": "Complete",
#                                     "status": "Match drawn",
#                                     "team1": {
#                                         "teamId": 145,
#                                         "teamName": "Leicestershire",
#                                         "teamSName": "LEIC",
#                                         "imageId": 172212,
#                                     },
#                                     "team2": {
#                                         "teamId": 150,
#                                         "teamName": "Kent",
#                                         "teamSName": "KENT",
#                                         "imageId": 172217,
#                                     },
#                                     "venueInfo": {
#                                         "id": 222,
#                                         "ground": "Grace Road",
#                                         "city": "Leicester",
#                                         "timezone": "+01:00",
#                                         "latitude": "52.607861",
#                                         "longitude": "-1.142709",
#                                     },
#                                     "seriesStartDt": "1743638400000",
#                                     "seriesEndDt": "1759017600000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "Complete",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 459,
#                                             "wickets": 7,
#                                             "overs": 84.1,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 17,
#                                             "overs": 9.1,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 113640,
#                                     "seriesId": 9369,
#                                     "seriesName": "County Championship Division Two 2025",
#                                     "matchDesc": "51st Match",
#                                     "matchFormat": "TEST",
#                                     "startDate": "1757928600000",
#                                     "endDate": "1758213000000",
#                                     "state": "Complete",
#                                     "status": "Gloucestershire won by 7 wkts",
#                                     "team1": {
#                                         "teamId": 142,
#                                         "teamName": "Northamptonshire",
#                                         "teamSName": "NHNTS",
#                                         "imageId": 172209,
#                                     },
#                                     "team2": {
#                                         "teamId": 151,
#                                         "teamName": "Gloucestershire",
#                                         "teamSName": "GLOUCS",
#                                         "imageId": 172218,
#                                     },
#                                     "venueInfo": {
#                                         "id": 63,
#                                         "ground": "County Ground",
#                                         "city": "Bristol",
#                                         "timezone": "+01:00",
#                                         "latitude": "51.477246",
#                                         "longitude": "-2.584212",
#                                     },
#                                     "currBatTeamId": 151,
#                                     "seriesStartDt": "1743638400000",
#                                     "seriesEndDt": "1759017600000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "GLOUCS Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 206,
#                                             "wickets": 10,
#                                             "overs": 63.5,
#                                         },
#                                         "inngs2": {
#                                             "inningsId": 3,
#                                             "runs": 192,
#                                             "wickets": 10,
#                                             "overs": 50.2,
#                                         },
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 241,
#                                             "wickets": 10,
#                                             "overs": 63.6,
#                                         },
#                                         "inngs2": {
#                                             "inningsId": 4,
#                                             "runs": 158,
#                                             "wickets": 3,
#                                             "overs": 23.6,
#                                         },
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 113634,
#                                     "seriesId": 9369,
#                                     "seriesName": "County Championship Division Two 2025",
#                                     "matchDesc": "50th Match",
#                                     "matchFormat": "TEST",
#                                     "startDate": "1757928600000",
#                                     "endDate": "1758213000000",
#                                     "state": "Complete",
#                                     "status": "Match Drawn",
#                                     "team1": {
#                                         "teamId": 74,
#                                         "teamName": "Middlesex",
#                                         "teamSName": "MDX",
#                                         "imageId": 172170,
#                                     },
#                                     "team2": {
#                                         "teamId": 143,
#                                         "teamName": "Lancashire",
#                                         "teamSName": "LANCS",
#                                         "imageId": 172210,
#                                     },
#                                     "venueInfo": {
#                                         "id": 65,
#                                         "ground": "Emirates Old Trafford",
#                                         "city": "Manchester",
#                                         "timezone": "+01:00",
#                                         "latitude": "53.463066",
#                                         "longitude": "-2.291301",
#                                     },
#                                     "seriesStartDt": "1743638400000",
#                                     "seriesEndDt": "1759017600000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "Complete",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 211,
#                                             "wickets": 10,
#                                             "overs": 50.4,
#                                         },
#                                         "inngs2": {
#                                             "inningsId": 3,
#                                             "runs": 99,
#                                             "wickets": 4,
#                                             "overs": 38.5,
#                                         },
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 375,
#                                             "wickets": 5,
#                                             "overs": 68.6,
#                                         }
#                                     },
#                                 },
#                             },
#                         ],
#                     }
#                 },
#             ],
#         },
#         {
#             "matchType": "Women",
#             "seriesMatches": [
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 9929,
#                         "seriesName": "Australia Women tour of India, 2025",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 119825,
#                                     "seriesId": 9929,
#                                     "seriesName": "Australia Women tour of India, 2025",
#                                     "matchDesc": "2nd ODI",
#                                     "matchFormat": "ODI",
#                                     "startDate": "1758096000000",
#                                     "endDate": "1758124800000",
#                                     "state": "Complete",
#                                     "status": "India Women won by 102 runs",
#                                     "team1": {
#                                         "teamId": 97,
#                                         "teamName": "India Women",
#                                         "teamSName": "INDW",
#                                         "imageId": 172189,
#                                     },
#                                     "team2": {
#                                         "teamId": 100,
#                                         "teamName": "Australia Women",
#                                         "teamSName": "AUSW",
#                                         "imageId": 172192,
#                                     },
#                                     "venueInfo": {
#                                         "id": 851,
#                                         "ground": "Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur",
#                                         "city": "New Chandigarh",
#                                         "timezone": "+05:30",
#                                         "latitude": "30.741797",
#                                         "longitude": "76.774915",
#                                     },
#                                     "currBatTeamId": 97,
#                                     "seriesStartDt": "1757721600000",
#                                     "seriesEndDt": "1758412800000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "INDW Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 292,
#                                             "wickets": 10,
#                                             "overs": 49.5,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 190,
#                                             "wickets": 10,
#                                             "overs": 40.5,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 119819,
#                                     "seriesId": 9929,
#                                     "seriesName": "Australia Women tour of India, 2025",
#                                     "matchDesc": "1st ODI",
#                                     "matchFormat": "ODI",
#                                     "startDate": "1757836800000",
#                                     "endDate": "1757865600000",
#                                     "state": "Complete",
#                                     "status": "Australia Women won by 8 wkts",
#                                     "team1": {
#                                         "teamId": 97,
#                                         "teamName": "India Women",
#                                         "teamSName": "INDW",
#                                         "imageId": 172189,
#                                     },
#                                     "team2": {
#                                         "teamId": 100,
#                                         "teamName": "Australia Women",
#                                         "teamSName": "AUSW",
#                                         "imageId": 172192,
#                                     },
#                                     "venueInfo": {
#                                         "id": 851,
#                                         "ground": "Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur",
#                                         "city": "New Chandigarh",
#                                         "timezone": "+05:30",
#                                         "latitude": "30.741797",
#                                         "longitude": "76.774915",
#                                     },
#                                     "currBatTeamId": 100,
#                                     "seriesStartDt": "1757721600000",
#                                     "seriesEndDt": "1758412800000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "AUSW Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 281,
#                                             "wickets": 7,
#                                             "overs": 49.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 282,
#                                             "wickets": 2,
#                                             "overs": 44.1,
#                                         }
#                                     },
#                                 },
#                             },
#                         ],
#                     }
#                 },
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 10702,
#                         "seriesName": "ICC Womens T20 World Cup East Asia Pacific Qualifier 2025",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 131867,
#                                     "seriesId": 10702,
#                                     "seriesName": "ICC Womens T20 World Cup East Asia Pacific Qualifier 2025",
#                                     "matchDesc": "7th Place Play-off",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757885400000",
#                                     "endDate": "1757898000000",
#                                     "state": "Complete",
#                                     "status": "Philippines Women won by 4 wkts",
#                                     "team1": {
#                                         "teamId": 1754,
#                                         "teamName": "Cook Islands Women",
#                                         "teamSName": "CISW",
#                                         "imageId": 341074,
#                                     },
#                                     "team2": {
#                                         "teamId": 1514,
#                                         "teamName": "Philippines Women",
#                                         "teamSName": "PHIW",
#                                         "imageId": 307469,
#                                     },
#                                     "venueInfo": {
#                                         "id": 1438123,
#                                         "ground": "Albert Park 2",
#                                         "city": "Suva",
#                                         "timezone": "+12:00",
#                                         "latitude": "-18.1471997",
#                                         "longitude": "178.4200685",
#                                     },
#                                     "currBatTeamId": 1514,
#                                     "seriesStartDt": "1757289600000",
#                                     "seriesEndDt": "1757980800000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "PHIW Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 115,
#                                             "wickets": 6,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 116,
#                                             "wickets": 6,
#                                             "overs": 19.4,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 131884,
#                                     "seriesId": 10702,
#                                     "seriesName": "ICC Womens T20 World Cup East Asia Pacific Qualifier 2025",
#                                     "matchDesc": "3rd place play-off",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757899800000",
#                                     "endDate": "1757912400000",
#                                     "state": "Complete",
#                                     "status": "Indonesia Women won by 8 wkts",
#                                     "team1": {
#                                         "teamId": 487,
#                                         "teamName": "Japan Women",
#                                         "teamSName": "JPNW",
#                                         "imageId": 248419,
#                                     },
#                                     "team2": {
#                                         "teamId": 484,
#                                         "teamName": "Indonesia Women",
#                                         "teamSName": "IDNW",
#                                         "imageId": 172532,
#                                     },
#                                     "venueInfo": {
#                                         "id": 1438123,
#                                         "ground": "Albert Park 2",
#                                         "city": "Suva",
#                                         "timezone": "+12:00",
#                                         "latitude": "-18.1471997",
#                                         "longitude": "178.4200685",
#                                     },
#                                     "currBatTeamId": 484,
#                                     "seriesStartDt": "1757289600000",
#                                     "seriesEndDt": "1757980800000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "IDNW Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 125,
#                                             "wickets": 7,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 128,
#                                             "wickets": 2,
#                                             "overs": 16.4,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 131873,
#                                     "seriesId": 10702,
#                                     "seriesName": "ICC Womens T20 World Cup East Asia Pacific Qualifier 2025",
#                                     "matchDesc": "Final",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757899800000",
#                                     "endDate": "1757912400000",
#                                     "state": "Complete",
#                                     "status": "Papua New Guinea Women won by 9 wkts",
#                                     "team1": {
#                                         "teamId": 506,
#                                         "teamName": "Vanuatu Women",
#                                         "teamSName": "VANW",
#                                         "imageId": 172555,
#                                     },
#                                     "team2": {
#                                         "teamId": 390,
#                                         "teamName": "Papua New Guinea Women",
#                                         "teamSName": "PNGW",
#                                         "imageId": 172443,
#                                     },
#                                     "venueInfo": {
#                                         "id": 1438120,
#                                         "ground": "Albert Park 1",
#                                         "city": "Suva",
#                                         "timezone": "+12:00",
#                                         "latitude": "-18.1472049",
#                                         "longitude": "178.4223645",
#                                     },
#                                     "currBatTeamId": 390,
#                                     "seriesStartDt": "1757289600000",
#                                     "seriesEndDt": "1757980800000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "PNGW Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 113,
#                                             "wickets": 9,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 114,
#                                             "wickets": 1,
#                                             "overs": 15.1,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 131856,
#                                     "seriesId": 10702,
#                                     "seriesName": "ICC Womens T20 World Cup East Asia Pacific Qualifier 2025",
#                                     "matchDesc": "5th Place Play-off",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757885400000",
#                                     "endDate": "1757898000000",
#                                     "state": "Complete",
#                                     "status": "Fiji Women won by 5 wkts",
#                                     "team1": {
#                                         "teamId": 482,
#                                         "teamName": "Samoa Women",
#                                         "teamSName": "WSMW",
#                                         "imageId": 172530,
#                                     },
#                                     "team2": {
#                                         "teamId": 1181,
#                                         "teamName": "Fiji Women",
#                                         "teamSName": "FIJIW",
#                                         "imageId": 248411,
#                                     },
#                                     "venueInfo": {
#                                         "id": 1438120,
#                                         "ground": "Albert Park 1",
#                                         "city": "Suva",
#                                         "timezone": "+12:00",
#                                         "latitude": "-18.1472049",
#                                         "longitude": "178.4223645",
#                                     },
#                                     "currBatTeamId": 1181,
#                                     "seriesStartDt": "1757289600000",
#                                     "seriesEndDt": "1757980800000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "FIJIW Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 74,
#                                             "wickets": 10,
#                                             "overs": 12.3,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 75,
#                                             "wickets": 5,
#                                             "overs": 13.5,
#                                         }
#                                     },
#                                 },
#                             },
#                         ],
#                     }
#                 },
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 10867,
#                         "seriesName": "Luxembourg Womens T20I Tri-Series, 2025",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 133847,
#                                     "seriesId": 10867,
#                                     "seriesName": "Luxembourg Womens T20I Tri-Series, 2025",
#                                     "matchDesc": "Final",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757853000000",
#                                     "endDate": "1757865600000",
#                                     "state": "Complete",
#                                     "status": "Switzerland Women won by 8 wkts",
#                                     "team1": {
#                                         "teamId": 1794,
#                                         "teamName": "Luxembourg Women",
#                                         "teamSName": "LUXW",
#                                         "imageId": 349590,
#                                     },
#                                     "team2": {
#                                         "teamId": 2390,
#                                         "teamName": "Switzerland Women",
#                                         "teamSName": "SUIW",
#                                         "imageId": 692942,
#                                     },
#                                     "venueInfo": {
#                                         "id": 719,
#                                         "ground": "Pierre Werner Cricket Ground",
#                                         "city": "Walferdange",
#                                         "timezone": "+02:00",
#                                         "latitude": "49.658611",
#                                         "longitude": "6.132490",
#                                     },
#                                     "currBatTeamId": 2390,
#                                     "seriesStartDt": "1757548800000",
#                                     "seriesEndDt": "1757894400000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "SUIW Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 81,
#                                             "wickets": 8,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 82,
#                                             "wickets": 2,
#                                             "overs": 10.3,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 133836,
#                                     "seriesId": 10867,
#                                     "seriesName": "Luxembourg Womens T20I Tri-Series, 2025",
#                                     "matchDesc": "3rd Place Play-off",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757838600000",
#                                     "endDate": "1757851200000",
#                                     "state": "Complete",
#                                     "status": "Luxembourg Women won by 8 wkts - 10-over game due to rain",
#                                     "team1": {
#                                         "teamId": 775,
#                                         "teamName": "Austria Women",
#                                         "teamSName": "AUTW",
#                                         "imageId": 274436,
#                                     },
#                                     "team2": {
#                                         "teamId": 1794,
#                                         "teamName": "Luxembourg Women",
#                                         "teamSName": "LUXW",
#                                         "imageId": 349590,
#                                     },
#                                     "venueInfo": {
#                                         "id": 719,
#                                         "ground": "Pierre Werner Cricket Ground",
#                                         "city": "Walferdange",
#                                         "timezone": "+02:00",
#                                         "latitude": "49.658611",
#                                         "longitude": "6.132490",
#                                     },
#                                     "currBatTeamId": 1794,
#                                     "seriesStartDt": "1757548800000",
#                                     "seriesEndDt": "1757894400000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "LUXW Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 63,
#                                             "wickets": 6,
#                                             "overs": 9.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 64,
#                                             "wickets": 2,
#                                             "overs": 9.5,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 133820,
#                                     "seriesId": 10867,
#                                     "seriesName": "Luxembourg Womens T20I Tri-Series, 2025",
#                                     "matchDesc": "2nd Match",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757752200000",
#                                     "endDate": "1757764800000",
#                                     "state": "Complete",
#                                     "status": "Austria Women won by 54 runs (DLS method) - Revised to 18 overs due to rain",
#                                     "team1": {
#                                         "teamId": 775,
#                                         "teamName": "Austria Women",
#                                         "teamSName": "AUTW",
#                                         "imageId": 274436,
#                                     },
#                                     "team2": {
#                                         "teamId": 1794,
#                                         "teamName": "Luxembourg Women",
#                                         "teamSName": "LUXW",
#                                         "imageId": 349590,
#                                     },
#                                     "venueInfo": {
#                                         "id": 719,
#                                         "ground": "Pierre Werner Cricket Ground",
#                                         "city": "Walferdange",
#                                         "timezone": "+02:00",
#                                         "latitude": "49.658611",
#                                         "longitude": "6.132490",
#                                     },
#                                     "currBatTeamId": 775,
#                                     "seriesStartDt": "1757548800000",
#                                     "seriesEndDt": "1757894400000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "AUTW Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 151,
#                                             "wickets": 1,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 86,
#                                             "wickets": 8,
#                                             "overs": 17.6,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 133831,
#                                     "seriesId": 10867,
#                                     "seriesName": "Luxembourg Womens T20I Tri-Series, 2025",
#                                     "matchDesc": "3rd Match",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757766600000",
#                                     "endDate": "1757779200000",
#                                     "state": "Complete",
#                                     "status": "Switzerland Women won by 6 wkts",
#                                     "team1": {
#                                         "teamId": 775,
#                                         "teamName": "Austria Women",
#                                         "teamSName": "AUTW",
#                                         "imageId": 274436,
#                                     },
#                                     "team2": {
#                                         "teamId": 2390,
#                                         "teamName": "Switzerland Women",
#                                         "teamSName": "SUIW",
#                                         "imageId": 692942,
#                                     },
#                                     "venueInfo": {
#                                         "id": 719,
#                                         "ground": "Pierre Werner Cricket Ground",
#                                         "city": "Walferdange",
#                                         "timezone": "+02:00",
#                                         "latitude": "49.658611",
#                                         "longitude": "6.132490",
#                                     },
#                                     "currBatTeamId": 2390,
#                                     "seriesStartDt": "1757548800000",
#                                     "seriesEndDt": "1757894400000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "SUIW Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 145,
#                                             "wickets": 6,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 146,
#                                             "wickets": 4,
#                                             "overs": 19.5,
#                                         }
#                                     },
#                                 },
#                             },
#                         ],
#                     }
#                 },
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 10141,
#                         "seriesName": "Womens Caribbean Premier League 2025",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 122137,
#                                     "seriesId": 10141,
#                                     "seriesName": "Womens Caribbean Premier League 2025",
#                                     "matchDesc": "6th Match",
#                                     "matchFormat": "T20",
#                                     "startDate": "1758049200000",
#                                     "endDate": "1758061800000",
#                                     "state": "Complete",
#                                     "status": "Barbados Royals Women won by 7 wkts",
#                                     "team1": {
#                                         "teamId": 1139,
#                                         "teamName": "Trinbago Knight Riders Women",
#                                         "teamSName": "TKRW",
#                                         "imageId": 241610,
#                                     },
#                                     "team2": {
#                                         "teamId": 1137,
#                                         "teamName": "Barbados Royals Women",
#                                         "teamSName": "BRW",
#                                         "imageId": 241608,
#                                     },
#                                     "venueInfo": {
#                                         "id": 110,
#                                         "ground": "Providence Stadium",
#                                         "city": "Guyana",
#                                         "timezone": "-04:00",
#                                         "latitude": "41.823872",
#                                         "longitude": "-71.411987",
#                                     },
#                                     "currBatTeamId": 1137,
#                                     "seriesStartDt": "1757030400000",
#                                     "seriesEndDt": "1758153600000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "BRW Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 148,
#                                             "wickets": 8,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 149,
#                                             "wickets": 3,
#                                             "overs": 19.1,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 122115,
#                                     "seriesId": 10141,
#                                     "seriesName": "Womens Caribbean Premier League 2025",
#                                     "matchDesc": "4th Match",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757793600000",
#                                     "endDate": "1757806200000",
#                                     "state": "Complete",
#                                     "status": "Guyana Amazon Warriors Women won by 5 wkts",
#                                     "team1": {
#                                         "teamId": 1139,
#                                         "teamName": "Trinbago Knight Riders Women",
#                                         "teamSName": "TKRW",
#                                         "imageId": 241610,
#                                     },
#                                     "team2": {
#                                         "teamId": 1144,
#                                         "teamName": "Guyana Amazon Warriors Women",
#                                         "teamSName": "GAWW",
#                                         "imageId": 241607,
#                                     },
#                                     "venueInfo": {
#                                         "id": 110,
#                                         "ground": "Providence Stadium",
#                                         "city": "Guyana",
#                                         "timezone": "-04:00",
#                                         "latitude": "41.823872",
#                                         "longitude": "-71.411987",
#                                     },
#                                     "currBatTeamId": 1144,
#                                     "seriesStartDt": "1757030400000",
#                                     "seriesEndDt": "1758153600000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "GAWW Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 123,
#                                             "wickets": 7,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 125,
#                                             "wickets": 5,
#                                             "overs": 18.5,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 122148,
#                                     "seriesId": 10141,
#                                     "seriesName": "Womens Caribbean Premier League 2025",
#                                     "matchDesc": "Final",
#                                     "matchFormat": "T20",
#                                     "startDate": "1758132000000",
#                                     "endDate": "1758144600000",
#                                     "state": "Complete",
#                                     "status": "Barbados Royals Women won by 3 wkts",
#                                     "team1": {
#                                         "teamId": 1144,
#                                         "teamName": "Guyana Amazon Warriors Women",
#                                         "teamSName": "GAWW",
#                                         "imageId": 241607,
#                                     },
#                                     "team2": {
#                                         "teamId": 1137,
#                                         "teamName": "Barbados Royals Women",
#                                         "teamSName": "BRW",
#                                         "imageId": 241608,
#                                     },
#                                     "venueInfo": {
#                                         "id": 110,
#                                         "ground": "Providence Stadium",
#                                         "city": "Guyana",
#                                         "timezone": "-04:00",
#                                         "latitude": "41.823872",
#                                         "longitude": "-71.411987",
#                                     },
#                                     "currBatTeamId": 1137,
#                                     "seriesStartDt": "1757030400000",
#                                     "seriesEndDt": "1758153600000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "BRW Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 136,
#                                             "wickets": 3,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 137,
#                                             "wickets": 7,
#                                             "overs": 19.4,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 122126,
#                                     "seriesId": 10141,
#                                     "seriesName": "Womens Caribbean Premier League 2025",
#                                     "matchDesc": "5th Match",
#                                     "matchFormat": "T20",
#                                     "startDate": "1757872800000",
#                                     "endDate": "1757885400000",
#                                     "state": "Complete",
#                                     "status": "Barbados Royals Women won by 3 runs",
#                                     "team1": {
#                                         "teamId": 1137,
#                                         "teamName": "Barbados Royals Women",
#                                         "teamSName": "BRW",
#                                         "imageId": 241608,
#                                     },
#                                     "team2": {
#                                         "teamId": 1144,
#                                         "teamName": "Guyana Amazon Warriors Women",
#                                         "teamSName": "GAWW",
#                                         "imageId": 241607,
#                                     },
#                                     "venueInfo": {
#                                         "id": 110,
#                                         "ground": "Providence Stadium",
#                                         "city": "Guyana",
#                                         "timezone": "-04:00",
#                                         "latitude": "41.823872",
#                                         "longitude": "-71.411987",
#                                     },
#                                     "currBatTeamId": 1137,
#                                     "seriesStartDt": "1757030400000",
#                                     "seriesEndDt": "1758153600000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "BRW Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 132,
#                                             "wickets": 6,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 129,
#                                             "wickets": 8,
#                                             "overs": 19.6,
#                                         }
#                                     },
#                                 },
#                             },
#                         ],
#                     }
#                 },
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 10845,
#                         "seriesName": "South Africa Women tour of Pakistan, 2025",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 133688,
#                                     "seriesId": 10845,
#                                     "seriesName": "South Africa Women tour of Pakistan, 2025",
#                                     "matchDesc": "1st ODI",
#                                     "matchFormat": "ODI",
#                                     "startDate": "1758018600000",
#                                     "endDate": "1758047400000",
#                                     "state": "Complete",
#                                     "status": "South Africa Women won by 8 wkts",
#                                     "team1": {
#                                         "teamId": 259,
#                                         "teamName": "Pakistan Women",
#                                         "teamSName": "PAKW",
#                                         "imageId": 172312,
#                                     },
#                                     "team2": {
#                                         "teamId": 260,
#                                         "teamName": "South Africa Women",
#                                         "teamSName": "RSAW",
#                                         "imageId": 172313,
#                                     },
#                                     "venueInfo": {
#                                         "id": 26,
#                                         "ground": "Gaddafi Stadium",
#                                         "city": "Lahore",
#                                         "timezone": "+05:00",
#                                         "latitude": "31.513467",
#                                         "longitude": "74.333375",
#                                     },
#                                     "currBatTeamId": 260,
#                                     "seriesStartDt": "1757894400000",
#                                     "seriesEndDt": "1758585600000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "RSAW Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 255,
#                                             "wickets": 4,
#                                             "overs": 49.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 259,
#                                             "wickets": 2,
#                                             "overs": 48.2,
#                                         }
#                                     },
#                                 },
#                             },
#                             {
#                                 "matchInfo": {
#                                     "matchId": 133693,
#                                     "seriesId": 10845,
#                                     "seriesName": "South Africa Women tour of Pakistan, 2025",
#                                     "matchDesc": "2nd ODI",
#                                     "matchFormat": "ODI",
#                                     "startDate": "1758277800000",
#                                     "endDate": "1758306600000",
#                                     "state": "Complete",
#                                     "status": "South Africa Women won by 25 runs by DLS Method (Target 313)",
#                                     "team1": {
#                                         "teamId": 260,
#                                         "teamName": "South Africa Women",
#                                         "teamSName": "RSAW",
#                                         "imageId": 172313,
#                                     },
#                                     "team2": {
#                                         "teamId": 259,
#                                         "teamName": "Pakistan Women",
#                                         "teamSName": "PAKW",
#                                         "imageId": 172312,
#                                     },
#                                     "venueInfo": {
#                                         "id": 26,
#                                         "ground": "Gaddafi Stadium",
#                                         "city": "Lahore",
#                                         "timezone": "+05:00",
#                                         "latitude": "31.513467",
#                                         "longitude": "74.333375",
#                                     },
#                                     "currBatTeamId": 260,
#                                     "seriesStartDt": "1757894400000",
#                                     "seriesEndDt": "1758585600000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "Complete",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 292,
#                                             "wickets": 3,
#                                             "overs": 45.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 287,
#                                             "wickets": 10,
#                                             "overs": 44.4,
#                                         }
#                                     },
#                                 },
#                             },
#                         ],
#                     }
#                 },
#             ],
#         },
#     ],
#     "filters": {"matchType": ["International", "League", "Domestic", "Women"]},
#     "appIndex": {
#         "seoTitle": "Live Cricket Score - Scorecard and Match Results",
#         "webURL": "www.cricbuzz.com/live-cricket-scores/",
#     },
#     "responseLastUpdated": "1758362761",
# }


# Live_match = {
#     "typeMatches": [
#         {
#             "matchType": "Domestic",
#             "seriesMatches": [
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 9273,
#                         "seriesName": "England Domestic One-Day Cup 2025",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 111985,
#                                     "seriesId": 9273,
#                                     "seriesName": "England Domestic One-Day Cup 2025",
#                                     "matchDesc": "Final",
#                                     "matchFormat": "ODI",
#                                     "startDate": "1758362400000",
#                                     "endDate": "1758391200000",
#                                     "state": "In Progress",
#                                     "status": "Worcestershire opt to bowl",
#                                     "team1": {
#                                         "teamId": 153,
#                                         "teamName": "Hampshire",
#                                         "teamSName": "HAM",
#                                         "imageId": 172220,
#                                     },
#                                     "team2": {
#                                         "teamId": 147,
#                                         "teamName": "Worcestershire",
#                                         "teamSName": "WORCS",
#                                         "imageId": 172214,
#                                     },
#                                     "venueInfo": {
#                                         "id": 18,
#                                         "ground": "Trent Bridge",
#                                         "city": "Nottingham",
#                                         "timezone": "+01:00",
#                                         "latitude": "52.936884",
#                                         "longitude": "-1.132230",
#                                     },
#                                     "currBatTeamId": 153,
#                                     "seriesStartDt": "1754265600000",
#                                     "seriesEndDt": "1758412800000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "In Progress",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 10,
#                                             "overs": 2.2,
#                                         }
#                                     }
#                                 },
#                             }
#                         ],
#                     }
#                 },
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 10829,
#                         "seriesName": "Australia Domestic One-Day Cup 2025-26",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 133479,
#                                     "seriesId": 10829,
#                                     "seriesName": "Australia Domestic One-Day Cup 2025-26",
#                                     "matchDesc": "4th Match",
#                                     "matchFormat": "ODI",
#                                     "startDate": "1758324600000",
#                                     "endDate": "1758353400000",
#                                     "state": "Complete",
#                                     "status": "New South Wales won by 131 runs",
#                                     "team1": {
#                                         "teamId": 104,
#                                         "teamName": "New South Wales",
#                                         "teamSName": "NSW",
#                                         "imageId": 172196,
#                                     },
#                                     "team2": {
#                                         "teamId": 158,
#                                         "teamName": "South Australia",
#                                         "teamSName": "SAUS",
#                                         "imageId": 172225,
#                                     },
#                                     "venueInfo": {
#                                         "id": 1727,
#                                         "ground": "Cricket Central",
#                                         "city": "Sydney",
#                                         "timezone": "+11:00",
#                                         "latitude": "-33.82595",
#                                         "longitude": "151.05187",
#                                     },
#                                     "currBatTeamId": 104,
#                                     "seriesStartDt": "1757894400000",
#                                     "seriesEndDt": "1772323200000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "NSW Won",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 288,
#                                             "wickets": 7,
#                                             "overs": 49.6,
#                                         }
#                                     },
#                                     "team2Score": {
#                                         "inngs1": {
#                                             "inningsId": 2,
#                                             "runs": 157,
#                                             "wickets": 10,
#                                             "overs": 36.3,
#                                         }
#                                     },
#                                 },
#                             }
#                         ],
#                     }
#                 },
#             ],
#         },
#         {
#             "matchType": "Women",
#             "seriesMatches": [
#                 {
#                     "seriesAdWrapper": {
#                         "seriesId": 9929,
#                         "seriesName": "Australia Women tour of India, 2025",
#                         "matches": [
#                             {
#                                 "matchInfo": {
#                                     "matchId": 119834,
#                                     "seriesId": 9929,
#                                     "seriesName": "Australia Women tour of India, 2025",
#                                     "matchDesc": "3rd ODI",
#                                     "matchFormat": "ODI",
#                                     "startDate": "1758355200000",
#                                     "endDate": "1758384000000",
#                                     "state": "In Progress",
#                                     "status": "Australia Women opt to bat",
#                                     "team1": {
#                                         "teamId": 100,
#                                         "teamName": "Australia Women",
#                                         "teamSName": "AUSW",
#                                         "imageId": 172192,
#                                     },
#                                     "team2": {
#                                         "teamId": 97,
#                                         "teamName": "India Women",
#                                         "teamSName": "INDW",
#                                         "imageId": 172189,
#                                     },
#                                     "venueInfo": {
#                                         "id": 51,
#                                         "ground": "Arun Jaitley Stadium",
#                                         "city": "Delhi",
#                                         "timezone": "+05:30",
#                                         "latitude": "28.637891",
#                                         "longitude": "77.243073",
#                                     },
#                                     "currBatTeamId": 100,
#                                     "seriesStartDt": "1757721600000",
#                                     "seriesEndDt": "1758412800000",
#                                     "isTimeAnnounced": True,
#                                     "stateTitle": "In Progress",
#                                 },
#                                 "matchScore": {
#                                     "team1Score": {
#                                         "inngs1": {
#                                             "inningsId": 1,
#                                             "runs": 219,
#                                             "wickets": 2,
#                                             "overs": 29.5,
#                                         }
#                                     }
#                                 },
#                             }
#                         ],
#                     }
#                 },
#                 {
#                     "ad": {
#                         "name": "native_matches",
#                         "layout": "native_large",
#                         "position": 3,
#                     }
#                 },
#             ],
#         },
#     ],
#     "filters": {"matchType": ["International", "League", "Domestic", "Women"]},
#     "appIndex": {
#         "seoTitle": "Live Cricket Score - Scorecard and Match Results",
#         "webURL": "www.cricbuzz.com/live-cricket-scores/",
#     },
#     "responseLastUpdated": "1758363121",
# }


# # ScoreCard of match id: 119834
# scard = {
#     "scorecard": [
#         {
#             "inningsid": 1,
#             "batsman": [
#                 {
#                     "id": 9113,
#                     "balls": 18,
#                     "runs": 30,
#                     "fours": 7,
#                     "sixes": 0,
#                     "strkrate": "166.67",
#                     "name": "Alyssa Healy",
#                     "nickname": "Alyssa Healy",
#                     "iscaptain": True,
#                     "iskeeper": True,
#                     "outdec": "c Harmanpreet Kaur b Kranti Gaud",
#                     "videotype": "",
#                     "videourl": "",
#                     "videoid": 0,
#                     "planid": 0,
#                     "imageid": 0,
#                     "premiumvideourl": "",
#                     "iscbplusfree": False,
#                     "ispremiumfree": False,
#                     "inmatchchange": "",
#                     "isoverseas": False,
#                     "playingxichange": "",
#                 },
#                 {
#                     "id": 18475,
#                     "balls": 68,
#                     "runs": 81,
#                     "fours": 14,
#                     "sixes": 0,
#                     "strkrate": "119.12",
#                     "name": "Georgia Voll",
#                     "nickname": "Georgia Voll",
#                     "iscaptain": False,
#                     "iskeeper": False,
#                     "outdec": "c (sub)Uma Chetry b Sneh Rana",
#                     "videotype": "",
#                     "videourl": "",
#                     "videoid": 0,
#                     "planid": 0,
#                     "imageid": 0,
#                     "premiumvideourl": "",
#                     "iscbplusfree": False,
#                     "ispremiumfree": False,
#                     "inmatchchange": "",
#                     "isoverseas": False,
#                     "playingxichange": "",
#                 },
#                 {
#                     "id": 9115,
#                     "balls": 72,
#                     "runs": 68,
#                     "fours": 7,
#                     "sixes": 2,
#                     "strkrate": "94.44",
#                     "name": "Ellyse Perry",
#                     "nickname": "Ellyse Perry",
#                     "iscaptain": False,
#                     "iskeeper": False,
#                     "outdec": "c Kranti Gaud b Arundhati Reddy",
#                     "videotype": "",
#                     "videourl": "",
#                     "videoid": 0,
#                     "planid": 0,
#                     "imageid": 0,
#                     "premiumvideourl": "",
#                     "iscbplusfree": False,
#                     "ispremiumfree": False,
#                     "inmatchchange": "",
#                     "isoverseas": False,
#                     "playingxichange": "",
#                 },
#                 {
#                     "id": 9989,
#                     "balls": 61,
#                     "runs": 108,
#                     "fours": 17,
#                     "sixes": 1,
#                     "strkrate": "177.05",
#                     "name": "Beth Mooney",
#                     "nickname": "Beth Mooney",
#                     "iscaptain": False,
#                     "iskeeper": False,
#                     "outdec": "batting",
#                     "videotype": "",
#                     "videourl": "",
#                     "videoid": 0,
#                     "planid": 0,
#                     "imageid": 0,
#                     "premiumvideourl": "",
#                     "iscbplusfree": False,
#                     "ispremiumfree": False,
#                     "inmatchchange": "",
#                     "isoverseas": False,
#                     "playingxichange": "",
#                 },
#                 {
#                     "id": 11989,
#                     "balls": 19,
#                     "runs": 24,
#                     "fours": 3,
#                     "sixes": 0,
#                     "strkrate": "126.32",
#                     "name": "Ashleigh Gardner",
#                     "nickname": "Ashleigh Gardner",
#                     "iscaptain": False,
#                     "iskeeper": False,
#                     "outdec": "batting",
#                     "videotype": "",
#                     "videourl": "",
#                     "videoid": 0,
#                     "planid": 0,
#                     "imageid": 0,
#                     "premiumvideourl": "",
#                     "iscbplusfree": False,
#                     "ispremiumfree": False,
#                     "inmatchchange": "",
#                     "isoverseas": False,
#                     "playingxichange": "",
#                 },
#                 {
#                     "id": 11101,
#                     "balls": 0,
#                     "runs": 0,
#                     "fours": 0,
#                     "sixes": 0,
#                     "strkrate": "0",
#                     "name": "Grace Harris",
#                     "nickname": "Grace Harris",
#                     "iscaptain": False,
#                     "iskeeper": False,
#                     "outdec": "",
#                     "videotype": "",
#                     "videourl": "",
#                     "videoid": 0,
#                     "planid": 0,
#                     "imageid": 0,
#                     "premiumvideourl": "",
#                     "iscbplusfree": False,
#                     "ispremiumfree": False,
#                     "inmatchchange": "",
#                     "isoverseas": False,
#                     "playingxichange": "IN",
#                 },
#                 {
#                     "id": 11956,
#                     "balls": 0,
#                     "runs": 0,
#                     "fours": 0,
#                     "sixes": 0,
#                     "strkrate": "0",
#                     "name": "Tahlia McGrath",
#                     "nickname": "Tahlia McGrath",
#                     "iscaptain": False,
#                     "iskeeper": False,
#                     "outdec": "",
#                     "videotype": "",
#                     "videourl": "",
#                     "videoid": 0,
#                     "planid": 0,
#                     "imageid": 0,
#                     "premiumvideourl": "",
#                     "iscbplusfree": False,
#                     "ispremiumfree": False,
#                     "inmatchchange": "",
#                     "isoverseas": False,
#                     "playingxichange": "",
#                 },
#                 {
#                     "id": 12015,
#                     "balls": 0,
#                     "runs": 0,
#                     "fours": 0,
#                     "sixes": 0,
#                     "strkrate": "0",
#                     "name": "Georgia Wareham",
#                     "nickname": "Georgia Wareham",
#                     "iscaptain": False,
#                     "iskeeper": False,
#                     "outdec": "",
#                     "videotype": "",
#                     "videourl": "",
#                     "videoid": 0,
#                     "planid": 0,
#                     "imageid": 0,
#                     "premiumvideourl": "",
#                     "iscbplusfree": False,
#                     "ispremiumfree": False,
#                     "inmatchchange": "",
#                     "isoverseas": False,
#                     "playingxichange": "",
#                 },
#                 {
#                     "id": 12002,
#                     "balls": 0,
#                     "runs": 0,
#                     "fours": 0,
#                     "sixes": 0,
#                     "strkrate": "0",
#                     "name": "Alana King",
#                     "nickname": "Alana King",
#                     "iscaptain": False,
#                     "iskeeper": False,
#                     "outdec": "",
#                     "videotype": "",
#                     "videourl": "",
#                     "videoid": 0,
#                     "planid": 0,
#                     "imageid": 0,
#                     "premiumvideourl": "",
#                     "iscbplusfree": False,
#                     "ispremiumfree": False,
#                     "inmatchchange": "",
#                     "isoverseas": False,
#                     "playingxichange": "",
#                 },
#                 {
#                     "id": 9476,
#                     "balls": 0,
#                     "runs": 0,
#                     "fours": 0,
#                     "sixes": 0,
#                     "strkrate": "0",
#                     "name": "Kim Garth",
#                     "nickname": "Kim Garth",
#                     "iscaptain": False,
#                     "iskeeper": False,
#                     "outdec": "",
#                     "videotype": "",
#                     "videourl": "",
#                     "videoid": 0,
#                     "planid": 0,
#                     "imageid": 0,
#                     "premiumvideourl": "",
#                     "iscbplusfree": False,
#                     "ispremiumfree": False,
#                     "inmatchchange": "",
#                     "isoverseas": False,
#                     "playingxichange": "IN",
#                 },
#                 {
#                     "id": 9108,
#                     "balls": 0,
#                     "runs": 0,
#                     "fours": 0,
#                     "sixes": 0,
#                     "strkrate": "0",
#                     "name": "Megan Schutt",
#                     "nickname": "Megan Schutt",
#                     "iscaptain": False,
#                     "iskeeper": False,
#                     "outdec": "",
#                     "videotype": "",
#                     "videourl": "",
#                     "videoid": 0,
#                     "planid": 0,
#                     "imageid": 0,
#                     "premiumvideourl": "",
#                     "iscbplusfree": False,
#                     "ispremiumfree": False,
#                     "inmatchchange": "",
#                     "isoverseas": False,
#                     "playingxichange": "",
#                 },
#             ],
#             "bowler": [
#                 {
#                     "id": 1448841,
#                     "overs": "6",
#                     "maidens": 0,
#                     "wickets": 1,
#                     "runs": 56,
#                     "economy": "9.3",
#                     "name": "Kranti Gaud",
#                     "nickname": "Kranti Gaud",
#                     "iscaptain": False,
#                     "iskeeper": False,
#                     "videotype": "",
#                     "videourl": "",
#                     "videoid": 0,
#                     "dots": 0,
#                     "balls": 36,
#                     "rpb": 0.0,
#                     "planid": 0,
#                     "imageid": 0,
#                     "premiumvideourl": "",
#                     "ispremiumfree": False,
#                     "inmatchchange": "",
#                     "isoverseas": False,
#                     "playingxichange": "",
#                 },
#                 {
#                     "id": 14491,
#                     "overs": "7",
#                     "maidens": 0,
#                     "wickets": 0,
#                     "runs": 47,
#                     "economy": "6.7",
#                     "name": "Renuka Singh Thakur",
#                     "nickname": "Renuka Singh",
#                     "iscaptain": False,
#                     "iskeeper": False,
#                     "videotype": "",
#                     "videourl": "",
#                     "videoid": 0,
#                     "dots": 0,
#                     "balls": 42,
#                     "rpb": 0.0,
#                     "planid": 0,
#                     "imageid": 0,
#                     "premiumvideourl": "",
#                     "ispremiumfree": False,
#                     "inmatchchange": "",
#                     "isoverseas": False,
#                     "playingxichange": "",
#                 },
#                 {
#                     "id": 11326,
#                     "overs": "8",
#                     "maidens": 0,
#                     "wickets": 1,
#                     "runs": 47,
#                     "economy": "5.9",
#                     "name": "Sneh Rana",
#                     "nickname": "Sneh Rana",
#                     "iscaptain": False,
#                     "iskeeper": False,
#                     "videotype": "",
#                     "videourl": "",
#                     "videoid": 0,
#                     "dots": 0,
#                     "balls": 48,
#                     "rpb": 0.0,
#                     "planid": 0,
#                     "imageid": 0,
#                     "premiumvideourl": "",
#                     "ispremiumfree": False,
#                     "inmatchchange": "",
#                     "isoverseas": False,
#                     "playingxichange": "",
#                 },
#                 {
#                     "id": 13661,
#                     "overs": "6",
#                     "maidens": 0,
#                     "wickets": 1,
#                     "runs": 56,
#                     "economy": "9.3",
#                     "name": "Arundhati Reddy",
#                     "nickname": "Arundhati Reddy",
#                     "iscaptain": False,
#                     "iskeeper": False,
#                     "videotype": "",
#                     "videourl": "",
#                     "videoid": 0,
#                     "dots": 0,
#                     "balls": 36,
#                     "rpb": 0.0,
#                     "planid": 0,
#                     "imageid": 0,
#                     "premiumvideourl": "",
#                     "ispremiumfree": False,
#                     "inmatchchange": "",
#                     "isoverseas": False,
#                     "playingxichange": "",
#                 },
#                 {
#                     "id": 11098,
#                     "overs": "8",
#                     "maidens": 0,
#                     "wickets": 0,
#                     "runs": 65,
#                     "economy": "8.1",
#                     "name": "Deepti Sharma",
#                     "nickname": "Deepti Sharma",
#                     "iscaptain": False,
#                     "iskeeper": False,
#                     "videotype": "",
#                     "videourl": "",
#                     "videoid": 0,
#                     "dots": 0,
#                     "balls": 48,
#                     "rpb": 0.0,
#                     "planid": 0,
#                     "imageid": 0,
#                     "premiumvideourl": "",
#                     "ispremiumfree": False,
#                     "inmatchchange": "",
#                     "isoverseas": False,
#                     "playingxichange": "",
#                 },
#                 {
#                     "id": 13533,
#                     "overs": "4",
#                     "maidens": 0,
#                     "wickets": 0,
#                     "runs": 48,
#                     "economy": "12",
#                     "name": "Radha Yadav",
#                     "nickname": "Radha Yadav",
#                     "iscaptain": False,
#                     "iskeeper": False,
#                     "videotype": "",
#                     "videourl": "",
#                     "videoid": 0,
#                     "dots": 0,
#                     "balls": 24,
#                     "rpb": 0.0,
#                     "planid": 0,
#                     "imageid": 0,
#                     "premiumvideourl": "",
#                     "ispremiumfree": False,
#                     "inmatchchange": "",
#                     "isoverseas": False,
#                     "playingxichange": "",
#                 },
#             ],
#             "fow": {
#                 "fow": [
#                     {
#                         "batsmanid": 9113,
#                         "batsmanname": "Alyssa Healy",
#                         "overnbr": 4.2,
#                         "runs": 43,
#                         "ballnbr": 26,
#                     },
#                     {
#                         "batsmanid": 18475,
#                         "batsmanname": "Georgia Voll",
#                         "overnbr": 21.1,
#                         "runs": 150,
#                         "ballnbr": 127,
#                     },
#                     {
#                         "batsmanid": 9115,
#                         "batsmanname": "Ellyse Perry",
#                         "overnbr": 32.6,
#                         "runs": 256,
#                         "ballnbr": 198,
#                     },
#                 ]
#             },
#             "extras": {
#                 "legbyes": 0,
#                 "byes": 0,
#                 "wides": 4,
#                 "noballs": 4,
#                 "penalty": 0,
#                 "total": 8,
#             },
#             "pp": {
#                 "powerplay": [
#                     {
#                         "id": 7,
#                         "ovrfrom": 0.1,
#                         "ovrto": 10.0,
#                         "pptype": "mandatory",
#                         "run": 77,
#                         "wickets": 0,
#                     }
#                 ]
#             },
#             "score": 319,
#             "wickets": 3,
#             "overs": 39.0,
#             "runrate": 8.18,
#             "batteamname": "Australia Women",
#             "batteamsname": "AUSW",
#             "isdeclared": False,
#             "isfollowon": False,
#             "ballnbr": 234,
#             "rpb": 1.36,
#             "partnership": {
#                 "partnership": [
#                     {
#                         "id": 0,
#                         "bat1id": 9113,
#                         "bat1name": "Healy",
#                         "bat1runs": 30,
#                         "bat1fours": 7,
#                         "bat1sixes": 0,
#                         "bat2id": 18475,
#                         "bat2name": "Georgia Voll",
#                         "bat2runs": 10,
#                         "bat2fours": 2,
#                         "bat2sixes": 0,
#                         "totalruns": 43,
#                         "totalballs": 26,
#                         "bat1balls": 18,
#                         "bat2balls": 9,
#                         "teamname": "",
#                         "teamid": 0,
#                         "bat1ones": 2,
#                         "bat1twos": 0,
#                         "bat1threes": 0,
#                         "bat1fives": 0,
#                         "bat1boundaries": 7,
#                         "bat1sixers": 0,
#                         "bat2ones": 2,
#                         "bat2twos": 0,
#                         "bat2threes": 0,
#                         "bat2fives": 0,
#                         "bat2boundaries": 2,
#                         "bat2sixers": 0,
#                     },
#                     {
#                         "id": 0,
#                         "bat1id": 9115,
#                         "bat1name": "Perry",
#                         "bat1runs": 35,
#                         "bat1fours": 4,
#                         "bat1sixes": 1,
#                         "bat2id": 18475,
#                         "bat2name": "Georgia Voll",
#                         "bat2runs": 71,
#                         "bat2fours": 12,
#                         "bat2sixes": 0,
#                         "totalruns": 107,
#                         "totalballs": 101,
#                         "bat1balls": 42,
#                         "bat2balls": 59,
#                         "teamname": "",
#                         "teamid": 0,
#                         "bat1ones": 13,
#                         "bat1twos": 0,
#                         "bat1threes": 0,
#                         "bat1fives": 0,
#                         "bat1boundaries": 4,
#                         "bat1sixers": 1,
#                         "bat2ones": 19,
#                         "bat2twos": 2,
#                         "bat2threes": 0,
#                         "bat2fives": 0,
#                         "bat2boundaries": 12,
#                         "bat2sixers": 0,
#                     },
#                     {
#                         "id": 0,
#                         "bat1id": 9115,
#                         "bat1name": "Perry",
#                         "bat1runs": 33,
#                         "bat1fours": 3,
#                         "bat1sixes": 1,
#                         "bat2id": 9989,
#                         "bat2name": "Mooney",
#                         "bat2runs": 71,
#                         "bat2fours": 10,
#                         "bat2sixes": 1,
#                         "totalruns": 106,
#                         "totalballs": 71,
#                         "bat1balls": 30,
#                         "bat2balls": 42,
#                         "teamname": "",
#                         "teamid": 0,
#                         "bat1ones": 15,
#                         "bat1twos": 0,
#                         "bat1threes": 0,
#                         "bat1fives": 0,
#                         "bat1boundaries": 3,
#                         "bat1sixers": 1,
#                         "bat2ones": 18,
#                         "bat2twos": 2,
#                         "bat2threes": 1,
#                         "bat2fives": 0,
#                         "bat2boundaries": 10,
#                         "bat2sixers": 1,
#                     },
#                     {
#                         "id": 0,
#                         "bat1id": 11989,
#                         "bat1name": "Gardner",
#                         "bat1runs": 24,
#                         "bat1fours": 3,
#                         "bat1sixes": 0,
#                         "bat2id": 9989,
#                         "bat2name": "Mooney",
#                         "bat2runs": 37,
#                         "bat2fours": 7,
#                         "bat2sixes": 0,
#                         "totalruns": 63,
#                         "totalballs": 36,
#                         "bat1balls": 19,
#                         "bat2balls": 19,
#                         "teamname": "",
#                         "teamid": 0,
#                         "bat1ones": 8,
#                         "bat1twos": 2,
#                         "bat1threes": 0,
#                         "bat1fives": 0,
#                         "bat1boundaries": 3,
#                         "bat1sixers": 0,
#                         "bat2ones": 7,
#                         "bat2twos": 1,
#                         "bat2threes": 0,
#                         "bat2fives": 0,
#                         "bat2boundaries": 7,
#                         "bat2sixers": 0,
#                     },
#                 ]
#             },
#         }
#     ],
#     "ismatchcomplete": False,
#     "appindex": {
#         "seotitle": "Cricket scorecard - INDW vs AUSW 3rd ODI,Australia Women tour of India, 2025 | Cricbuzz.com",
#         "weburl": "http://www.cricbuzz.com/live-cricket-scorecard/119834/indw-vs-ausw-3rd-odi-australia-women-tour-of-india-2025",
#     },
#     "status": "Australia Women opt to bat",
#     "responselastupdated": 1758365658,
# }

# matchs_info = Live_match["typeMatches"]
# _scard = []
# match_link = scard.get("appindex", "").get("weburl", "")
# for match_scard in scard["scorecard"]:
#     if match_scard["inningsid"]:
#         innings_batting_scard = []

#         # Fetch Batting Scorecard
#         for batsman in match_scard["batsman"]:
#             innings_batting_scard.append(
#                 {
#                     "name": batsman["name"],
#                     "runs": batsman["runs"],
#                     "balls": batsman["balls"],
#                     "fours": batsman["fours"],
#                     "sixes": batsman["sixes"],
#                     "strike_rate": float(batsman["strkrate"]),
#                     "out_decision": (
#                         batsman["outdec"] if batsman["outdec"] else "Not Out"
#                     ),
#                 }
#             )

#             # Fetch Balling Scorecard
#             innings_bowling_scard = []
#             for bowler in match_scard["bowler"]:
#                 innings_bowling_scard.append(
#                     {
#                         "name": bowler["name"],
#                         "overs": bowler["overs"],
#                         "maidens": bowler["maidens"],
#                         "runs": bowler["runs"],
#                         "wickets": bowler["wickets"],
#                         "economy": float(bowler["economy"]),
#                     }
#                 )

#             _scard.append(
#                 {
#                     "inningsid": match_scard["inningsid"],
#                     "batteamname": match_scard["batteamname"],
#                     "batteamsname": match_scard["batteamsname"],
#                     "score": match_scard["score"],
#                     "wickets": match_scard["wickets"],
#                     "overs": match_scard["overs"],
#                     "runrate": match_scard["runrate"],
#                     "extras": match_scard.get("extras", {}).get("total", 0),
#                     "batting": innings_batting_scard,
#                     "bowling": innings_bowling_scard,
#                 }
#             )


# matches = []

# # Fetch Current Live Mathc Informations
# for type_match in Live_match.get("typeMatches", []):
#     for series_match in type_match.get("seriesMatches", []):
#         series_data = series_match.get("seriesAdWrapper", {})
#         series_id = series_data.get("seriesId")
#         series_name = series_data.get("seriesName")

#         for match in series_data.get("matches", []):
#             info = match.get("matchInfo", {})
#             match_id = info.get("matchId")
#             match_desc = info.get("matchDesc")
#             match_format = info.get("matchFormat")
#             start_date = info.get("startDate")
#             team1 = info.get("team1", {}).get("teamName")
#             team2 = info.get("team2", {}).get("teamName")
#             status = info.get("status")
#             venue = info.get("venueInfo", {}).get("ground")

#             matches.append(
#                 {
#                     "series_id": series_id,
#                     "series_name": series_name,
#                     "match_id": match_id,
#                     "match_desc": match_desc,
#                     "match_format": match_format,
#                     "start_date": start_date,
#                     "team1": team1,
#                     "team2": team2,
#                     "venue": venue,
#                     "status": status,
#                 }
#             )

# # Convert to DataFrame
# df = pd.DataFrame(
#     matches,
#     columns=[
#         "series_id",
#         "series_name",
#         "match_id",
#         "match_desc",
#         "match_format",
#         "start_date",
#         "team1",
#         "team2",
#         "venue",
#         "status",
#     ],
# )
# print(df)


# top_states = {
#     "filter": {
#         "matchtype": [
#             {"matchTypeId": "1", "matchTypeDesc": "test"},
#             {"matchTypeId": "2", "matchTypeDesc": "odi"},
#             {"matchTypeId": "3", "matchTypeDesc": "t20"},
#         ],
#         "team": [
#             {"id": "96", "teamShortName": "AFG"},
#             {"id": "13", "teamShortName": "NZ"},
#             {"id": "12", "teamShortName": "ZIM"},
#             {"id": "11", "teamShortName": "RSA"},
#             {"id": "10", "teamShortName": "WI"},
#             {"id": "9", "teamShortName": "ENG"},
#             {"id": "6", "teamShortName": "BAN"},
#             {"id": "5", "teamShortName": "SL"},
#             {"id": "4", "teamShortName": "AUS"},
#             {"id": "3", "teamShortName": "PAK"},
#             {"id": "27", "teamShortName": "IRE"},
#             {"id": "2", "teamShortName": "IND"},
#         ],
#         "selectedMatchType": "test",
#     },
#     "headers": ["Batter", "M", "I", "R", "Avg"],
#     "values": [
#         {"values": ["25", "Tendulkar", "200", "329", "15921", "53.79"]},
#         {"values": ["8019", "Root", "158", "288", "13543", "51.30"]},
#         {"values": ["38", "R Ponting", "168", "287", "13378", "51.85"]},
#         {"values": ["213", "Kallis", "166", "280", "13289", "55.37"]},
#         {"values": ["27", "Dravid", "164", "286", "13288", "52.31"]},
#         {"values": ["488", "Cook", "161", "291", "12472", "45.35"]},
#         {"values": ["104", "Sangakkara", "134", "233", "12400", "57.14"]},
#         {"values": ["240", "B Lara", "131", "232", "11953", "52.89"]},
#         {"values": ["244", "Chanderpaul", "164", "280", "11867", "51.37"]},
#         {"values": ["101", "Mahela", "149", "252", "11814", "49.85"]},
#         {"values": ["4672", "A Border", "156", "265", "11174", "50.56"]},
#         {"values": ["4712", "S Waugh", "168", "260", "10927", "51.06"]},
#         {"values": ["2250", "Steven Smith", "119", "212", "10477", "56.03"]},
#         {"values": ["3817", "S Gavaskar", "125", "214", "10122", "51.12"]},
#         {"values": ["130", "Younis Khan", "118", "213", "10099", "52.06"]},
#         {"values": ["314", "Amla", "124", "215", "9282", "46.64"]},
#         {"values": ["6326", "Williamson", "105", "186", "9276", "54.89"]},
#         {"values": ["207", "Graeme Smith", "117", "205", "9265", "48.26"]},
#         {"values": ["1413", "Kohli", "123", "210", "9230", "46.85"]},
#         {"values": ["5308", "G Gooch", "118", "215", "8900", "42.58"]},
#     ],
#     "appIndex": {
#         "seoTitle": "Live cricket scores, schedule, news, archive, series | Cricbuzz.com",
#         "webURL": "www.cricbuzz.com",
#     },
# }

import pandas as pd


Player_search = {
    "player": [
        {
            "id": "13376",
            "name": "Sachin Bhudia",
            "teamName": "Kenya",
            "faceImageId": "153979",
            "dob": "1998-09-24",
        },
        {
            "id": "14905",
            "name": "Sachin Mevada ",
            "teamName": "India",
            "faceImageId": "169688",
            "dob": "1999-04-23",
        },
        {
            "id": "25",
            "name": "Sachin Tendulkar",
            "teamName": "India",
            "faceImageId": "171004",
            "dob": "1973-04-24",
        },
        {
            "id": "1891",
            "name": "Sachin Rana",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "1984-09-18",
        },
        {
            "id": "8709",
            "name": "Sachin Baby",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "1988-12-18",
        },
        {
            "id": "8882",
            "name": "Sachin Chaudhari",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "1986-03-27",
        },
        {
            "id": "9296",
            "name": "Sachin Hooda",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "1988-08-27",
        },
        {
            "id": "9692",
            "name": "Sachin Mohan",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "1990-04-10",
        },
        {
            "id": "10308",
            "name": "Sachin Omprakash Katariya",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "1995-04-14",
        },
        {
            "id": "10602",
            "name": "Sachin Joshi",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "1984-08-07",
        },
        {
            "id": "11409",
            "name": "Audhi Sachin",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "N/A",
        },
        {
            "id": "11724",
            "name": "Sachin Gankal",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "1995-03-28",
        },
        {
            "id": "11760",
            "name": "Sachin Shinde",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "1987-09-29",
        },
        {
            "id": "11840",
            "name": "Sachin Solanki",
            "teamName": "United Arab Emirates",
            "faceImageId": "182026",
            "dob": "N/A",
        },
        {
            "id": "12378",
            "name": "Sachin Rathi",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "2003-11-03",
        },
        {
            "id": "12917",
            "name": "Sachin Sharma",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "N/A",
        },
        {
            "id": "13076",
            "name": "Lal Sachin",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "N/A",
        },
        {
            "id": "13691",
            "name": "Sachintha Peiris",
            "teamName": "Sri Lanka",
            "faceImageId": "182026",
            "dob": "1995-11-16",
        },
        {
            "id": "14966",
            "name": "Sachin Madhuker Yadav",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "1994-04-07",
        },
        {
            "id": "15012",
            "name": "Sachin Wagh",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "N/A",
        },
        {
            "id": "15490",
            "name": "Sachin Kumar",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "1997-12-25",
        },
        {
            "id": "15667",
            "name": "Sachindu Colombage",
            "teamName": "Sri Lanka",
            "faceImageId": "182026",
            "dob": "1998-02-21",
        },
        {
            "id": "21793",
            "name": "Sachini Nisansala",
            "teamName": "Sri Lanka",
            "faceImageId": "182026",
            "dob": "2001-11-10",
        },
        {
            "id": "26346",
            "name": "Sachin Mandy Gangareddy",
            "teamName": "Germany",
            "faceImageId": "182026",
            "dob": "1991-06-07",
        },
        {
            "id": "27039",
            "name": "Sachini Jayasinghe",
            "teamName": "Bahrain",
            "faceImageId": "182026",
            "dob": "1996-08-22",
        },
        {
            "id": "28199",
            "name": "Sachin Ganpat Shinde",
            "teamName": "Serbia",
            "faceImageId": "182026",
            "dob": "1983-11-15",
        },
        {
            "id": "29480",
            "name": "Sachin Kumar",
            "teamName": "Bahrain",
            "faceImageId": "182026",
            "dob": "1989-04-03",
        },
        {
            "id": "34144",
            "name": "Suresh Sachin",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "1998-01-02",
        },
        {
            "id": "46317",
            "name": "Sachin Singh Rathi",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "1987-04-30",
        },
        {
            "id": "46559",
            "name": "Balasubramaniam Sachin",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "2003-08-30",
        },
        {
            "id": "48599",
            "name": "Sachin Parmar",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "1999-04-23",
        },
        {
            "id": "49396",
            "name": "Sachin Kakodia",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "N/A",
        },
        {
            "id": "49443",
            "name": "Sachin Malav",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "N/A",
        },
        {
            "id": "49499",
            "name": "Sachin Yadav",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "2003-12-29",
        },
        {
            "id": "51798",
            "name": "Sachin Dhas",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "2005-02-03",
        },
        {
            "id": "52222",
            "name": "Sachin Bhosale",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "1998-01-02",
        },
        {
            "id": "52379",
            "name": "Sachin Sharma",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "1993-09-21",
        },
        {
            "id": "55312",
            "name": "Sachin Banamali",
            "teamName": "Singapore",
            "faceImageId": "182026",
            "dob": "1989-08-17",
        },
        {
            "id": "1424248",
            "name": "Sachin Ravikumar",
            "teamName": "Costa Rica",
            "faceImageId": "182026",
            "dob": "1988-05-27",
        },
        {
            "id": "1431361",
            "name": "Sachin Gill",
            "teamName": "Kenya",
            "faceImageId": "182026",
            "dob": "1996-12-04",
        },
        {
            "id": "1454129",
            "name": "Sachin Pawar",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "2007-06-06",
        },
        {
            "id": "1456754",
            "name": "Sachin B",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "2006-08-14",
        },
        {
            "id": "1460509",
            "name": "Sachin PS",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "1998-01-15",
        },
        {
            "id": "1461506",
            "name": "Sachin Singh",
            "teamName": "India",
            "faceImageId": "182026",
            "dob": "2002-11-19",
        },
    ],
    "category": "Sachin",
}

player_profile = {
    "id": "25",
    "bat": "Right Handed Bat",
    "bowl": "Right-arm legbreak",
    "name": "Sachin Tendulkar",
    "nickName": "Tendulkar",
    "height": "5 ft 5 in",
    "role": "Batsman",
    "birthPlace": "Bombay (now Mumbai), Maharashtra",
    "intlTeam": "India",
    "teams": "India, Asia XI, Mumbai, Mumbai Indians, Marylebone Cricket Club, Sachin Blasters, India Legends, India Masters",
    "DoB": "April 24, 1973 (52 years)",
    "image": "http://i.cricketcb.com/stats/img/faceImages/25.jpg",
    "rankings": {
        "bat": {"testBestRank": "1", "odiBestRank": "1", "t20BestRank": "63"},
        "bowl": {"testBestRank": "56", "odiBestRank": "41", "t20BestRank": "56"},
        "all": {"testBestRank": "8", "odiBestRank": "2"},
    },
    "appIndex": {
        "seoTitle": "Sachin Tendulkar Profile - Cricbuzz | Cricbuzz.com",
        "webURL": "http://www.cricbuzz.com/profiles/25/sachin-tendulkar",
    },
    "DoBFormat": "April 24, 1973",
    "faceImageId": 171004,
    "teamNameIds": [
        {"teamId": "2", "teamName": "India"},
        {"teamId": "37", "teamName": "Asia XI"},
        {"teamId": "95", "teamName": "Mumbai"},
        {"teamId": "62", "teamName": "Mumbai Indians"},
        {"teamId": "290", "teamName": "Marylebone Cricket Club"},
        {"teamId": "316", "teamName": "Sachin Blasters"},
        {"teamId": "682", "teamName": "India Legends"},
        {"teamId": "2326", "teamName": "India Masters"},
    ],
    "playerTeamIds": "2, 37, 95, 62, 290, 316, 682, 2326",
    "intlTeamImageId": 719031,
    "recentBatting": {
        "headers": ["OPPN.", "Score", "Format", "Date"],
        "rows": [
            {
                "values": ["13080", "WI", "74(118) & DNB", "Test", "14 Nov 13"],
                "followUpLinkText": "/live-cricket-scores/13080/ind-vs-wi-2nd-test-west-indies-in-india-2013",
            },
            {
                "values": ["13079", "WI", "10(24) & DNB", "Test", "06 Nov 13"],
                "followUpLinkText": "/live-cricket-scores/13079/ind-vs-wi-1st-test-west-indies-in-india-2013",
            },
            {
                "values": ["11945", "AUS", "32(53) & 1(5)", "Test", "22 Mar 13"],
                "followUpLinkText": "/live-cricket-scores/11945/ind-vs-aus-4th-test-australia-tour-of-india-2013",
            },
            {
                "values": ["11944", "AUS", "37(81) & 21(23)", "Test", "14 Mar 13"],
                "followUpLinkText": "/live-cricket-scores/11944/ind-vs-aus-3rd-test-australia-tour-of-india-2013",
            },
            {
                "values": ["11943", "AUS", "7(15) & DNB", "Test", "02 Mar 13"],
                "followUpLinkText": "/live-cricket-scores/11943/ind-vs-aus-2nd-test-australia-tour-of-india-2013",
            },
        ],
    },
    "recentBowling": {
        "headers": ["OPPN.", "Wickets", "Format", "Date"],
        "rows": [
            {
                "values": ["13080", "WI", "DNB & 0-8", "Test", "14 Nov 13"],
                "followUpLinkText": "/live-cricket-scores/13080/ind-vs-wi-2nd-test-west-indies-in-india-2013",
            },
            {
                "values": ["13079", "WI", "1-5 & 0-18", "Test", "06 Nov 13"],
                "followUpLinkText": "/live-cricket-scores/13079/ind-vs-wi-1st-test-west-indies-in-india-2013",
            },
            {
                "values": ["11944", "AUS", "DNB & 0-2", "Test", "14 Mar 13"],
                "followUpLinkText": "/live-cricket-scores/11944/ind-vs-aus-3rd-test-australia-tour-of-india-2013",
            },
            {
                "values": ["11346", "ENG", "DNB & 0-8", "Test", "15 Nov 12"],
                "followUpLinkText": "/live-cricket-scores/11346/ind-vs-eng-1st-test-england-tour-of-india-2012-13",
            },
            {
                "values": ["11342", "NZ", "0-6 & DNB", "Test", "23 Aug 12"],
                "followUpLinkText": "/live-cricket-scores/11342/ind-vs-nz-1st-test-new-zealand-tour-of-india-2012",
            },
        ],
    },
}

player_batting_stats = {
    "headers": ["ROWHEADER", "Test", "ODI", "T20", "IPL"],
    "values": [
        {"values": ["Matches", "63", "85", "72", "145"]},
        {"values": ["Innings", "111", "79", "68", "136"]},
        {"values": ["Runs", "3789", "3043", "2265", "5222"]},
        {"values": ["Balls", "7234", "3451", "1628", "3839"]},
        {"values": ["Highest", "199", "112", "110", "132"]},
        {"values": ["Average", "35.41", "49.08", "37.75", "46.21"]},
        {"values": ["SR", "52.38", "88.18", "139.13", "136.03"]},
        {"values": ["Not Out", "4", "17", "8", "23"]},
        {"values": ["Fours", "455", "235", "191", "452"]},
        {"values": ["Sixes", "26", "67", "99", "208"]},
        {"values": ["Ducks", "9", "3", "5", "4"]},
        {"values": ["50s", "19", "18", "22", "40"]},
        {"values": ["100s", "10", "7", "2", "5"]},
        {"values": ["200s", "0", "0", "0", "0"]},
        {"values": ["300s", "0", "0", "0", "0"]},
        {"values": ["400s", "0", "0", "0", "0"]},
    ],
    "appIndex": {
        "seoTitle": "KL Rahul Profile - Cricbuzz | Cricbuzz.com",
        "webURL": "http://www.cricbuzz.com/profiles/8733/kl-rahul",
    },
    "seriesSpinner": [{"seriesName": "Career"}],
}


batting_stats = {
    "Header": [],
    "Test": [],
    "ODI": [],
    "T20": [],
    "IPL": [],
}
for stats in player_batting_stats.get("values", []):
    batting_stats["Header"].append(stats["values"][0])
    batting_stats["Test"].append(stats["values"][1])
    batting_stats["ODI"].append(stats["values"][2])
    batting_stats["T20"].append(stats["values"][3])
    batting_stats["IPL"].append(stats["values"][4])

header = batting_stats.pop("Header")
print(header)
batting_df = pd.DataFrame(
    batting_stats, index=list(header), columns=["Test", "ODI", "T20", "IPL"]
)
print(batting_df)
total_matches = pd.to_numeric(batting_df.loc["Matches"], errors="coerce").sum()
print(f"{total_matches}")


# data = pd.DataFrame(
#     batting_stats,
#     columns=[
#         "Test",
#         "ODI",
#         "T20",
#         "IPL",
#     ],
#     index=batting_stats["Header"],
# )

# print(batting_stats)


# player_bowling_stats = {
#     "headers": ["ROWHEADER", "Test", "ODI", "T20", "IPL"],
#     "values": [
#         {"values": ["Matches", "200", "463", "1", "78"]},
#         {"values": ["Innings", "145", "270", "1", "4"]},
#         {"values": ["Balls", "4240", "8054", "15", "36"]},
#         {"values": ["Runs", "2492", "6850", "12", "58"]},
#         {"values": ["Maidens", "83", "24", "0", "0"]},
#         {"values": ["Wickets", "46", "154", "1", "0"]},
#         {"values": ["Avg", "54.17", "44.48", "12.0", "0.0"]},
#         {"values": ["Eco", "3.53", "5.1", "4.8", "9.67"]},
#         {"values": ["SR", "92.17", "52.3", "15.0", "0.0"]},
#         {"values": ["BBI", "3/10", "5/32", "1/12", "0/7"]},
#         {"values": ["BBM", "3/14", "5/32", "1/12", "0/7"]},
#         {"values": ["4w", "0", "4", "0", "0"]},
#         {"values": ["5w", "0", "2", "0", "0"]},
#         {"values": ["10w", "0", "0", "0", "0"]},
#     ],
#     "appIndex": {
#         "seoTitle": "Sachin Tendulkar Profile - Cricbuzz | Cricbuzz.com",
#         "webURL": "http://www.cricbuzz.com/profiles/25/sachin-tendulkar",
#     },
#     "seriesSpinner": [{"seriesName": "Career"}],
# }
