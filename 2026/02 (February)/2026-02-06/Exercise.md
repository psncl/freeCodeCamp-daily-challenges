# 2026 Winter Games Day 1: Opening Day

https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-06

Today marks the start of the 2026 Winter Games. The next 17 days will bring you coding challenges inspired by them.

For the first one, you are given a two-letter country code and need to return the flag emoji for that country.

Use this list:

| Country                |   Code |  Flag  |
| ---------------------- | -----: | :----: |
| Albania                | `"AL"` | `"🇦🇱"` |
| Andorra                | `"AD"` | `"🇦🇩"` |
| Argentina              | `"AR"` | `"🇦🇷"` |
| Armenia                | `"AM"` | `"🇦🇲"` |
| Australia              | `"AU"` | `"🇦🇺"` |
| Austria                | `"AT"` | `"🇦🇹"` |
| Azerbaijan             | `"AZ"` | `"🇦🇿"` |
| Belgium                | `"BE"` | `"🇧🇪"` |
| Benin                  | `"BJ"` | `"🇧🇯"` |
| Bolivia                | `"BO"` | `"🇧🇴"` |
| Bosnia and Herzegovina | `"BA"` | `"🇧🇦"` |
| Brazil                 | `"BR"` | `"🇧🇷"` |
| Bulgaria               | `"BG"` | `"🇧🇬"` |
| Canada                 | `"CA"` | `"🇨🇦"` |
| Chile                  | `"CL"` | `"🇨🇱"` |
| China                  | `"CN"` | `"🇨🇳"` |
| Colombia               | `"CO"` | `"🇨🇴"` |
| Croatia                | `"HR"` | `"🇭🇷"` |
| Cyprus                 | `"CY"` | `"🇨🇾"` |
| Czech Republic         | `"CZ"` | `"🇨🇿"` |
| Denmark                | `"DK"` | `"🇩🇰"` |
| Ecuador                | `"EC"` | `"🇪🇨"` |
| Eritrea                | `"ER"` | `"🇪🇷"` |
| Estonia                | `"EE"` | `"🇪🇪"` |
| Finland                | `"FI"` | `"🇫🇮"` |
| France                 | `"FR"` | `"🇫🇷"` |
| Georgia                | `"GE"` | `"🇬🇪"` |
| Germany                | `"DE"` | `"🇩🇪"` |
| Great Britain          | `"GB"` | `"🇬🇧"` |
| Greece                 | `"GR"` | `"🇬🇷"` |
| Guinea-Bissau          | `"GW"` | `"🇬🇼"` |
| Haiti                  | `"HT"` | `"🇭🇹"` |
| Hong Kong              | `"HK"` | `"🇭🇰"` |
| Hungary                | `"HU"` | `"🇭🇺"` |
| Iceland                | `"IS"` | `"🇮🇸"` |
| India                  | `"IN"` | `"🇮🇳"` |
| Iran                   | `"IR"` | `"🇮🇷"` |
| Ireland                | `"IE"` | `"🇮🇪"` |
| Israel                 | `"IL"` | `"🇮🇱"` |
| Italy                  | `"IT"` | `"🇮🇹"` |
| Jamaica                | `"JM"` | `"🇯🇲"` |
| Japan                  | `"JP"` | `"🇯🇵"` |
| Kazakhstan             | `"KZ"` | `"🇰🇿"` |
| Kenya                  | `"KE"` | `"🇰🇪"` |
| Kosovo                 | `"XK"` | `"🇽🇰"` |
| Kyrgyzstan             | `"KG"` | `"🇰🇬"` |
| Latvia                 | `"LV"` | `"🇱🇻"` |
| Lebanon                | `"LB"` | `"🇱🇧"` |
| Liechtenstein          | `"LI"` | `"🇱🇮"` |
| Lithuania              | `"LT"` | `"🇱🇹"` |
| Luxembourg             | `"LU"` | `"🇱🇺"` |
| Madagascar             | `"MG"` | `"🇲🇬"` |
| Malaysia               | `"MY"` | `"🇲🇾"` |
| Malta                  | `"MT"` | `"🇲🇹"` |
| Mexico                 | `"MX"` | `"🇲🇽"` |
| Moldova                | `"MD"` | `"🇲🇩"` |
| Monaco                 | `"MC"` | `"🇲🇨"` |
| Mongolia               | `"MN"` | `"🇲🇳"` |
| Montenegro             | `"ME"` | `"🇲🇪"` |
| Morocco                | `"MA"` | `"🇲🇦"` |
| Netherlands            | `"NL"` | `"🇳🇱"` |
| New Zealand            | `"NZ"` | `"🇳🇿"` |
| Nigeria                | `"NG"` | `"🇳🇬"` |
| North Macedonia        | `"MK"` | `"🇲🇰"` |
| Norway                 | `"NO"` | `"🇳🇴"` |
| Pakistan               | `"PK"` | `"🇵🇰"` |
| Philippines            | `"PH"` | `"🇵🇭"` |
| Poland                 | `"PL"` | `"🇵🇱"` |
| Portugal               | `"PT"` | `"🇵🇹"` |
| Puerto Rico            | `"PR"` | `"🇵🇷"` |
| Romania                | `"RO"` | `"🇷🇴"` |
| San Marino             | `"SM"` | `"🇸🇲"` |
| Saudi Arabia           | `"SA"` | `"🇸🇦"` |
| Serbia                 | `"RS"` | `"🇷🇸"` |
| Singapore              | `"SG"` | `"🇸🇬"` |
| Slovakia               | `"SK"` | `"🇸🇰"` |
| Slovenia               | `"SI"` | `"🇸🇮"` |
| South Africa           | `"ZA"` | `"🇿🇦"` |
| South Korea            | `"KR"` | `"🇰🇷"` |
| Spain                  | `"ES"` | `"🇪🇸"` |
| Sweden                 | `"SE"` | `"🇸🇪"` |
| Switzerland            | `"CH"` | `"🇨🇭"` |
| Thailand               | `"TH"` | `"🇹🇭"` |
| Trinidad & Tobago      | `"TT"` | `"🇹🇹"` |
| Turkey                 | `"TR"` | `"🇹🇷"` |
| Ukraine                | `"UA"` | `"🇺🇦"` |
| United Arab Emirates   | `"AE"` | `"🇦🇪"` |
| United States          | `"US"` | `"🇺🇸"` |
| Uruguay                | `"UY"` | `"🇺🇾"` |
| Uzbekistan             | `"UZ"` | `"🇺🇿"` |
| Venezuela              | `"VE"` | `"🇻🇪"` |

## Tests

1. get_flag("AL") should return "🇦🇱".
1. get_flag("AD") should return "🇦🇩".
1. get_flag("AR") should return "🇦🇷".
1. get_flag("AM") should return "🇦🇲".
1. get_flag("AU") should return "🇦🇺".
1. get_flag("AT") should return "🇦🇹".
1. get_flag("AZ") should return "🇦🇿".
1. get_flag("BE") should return "🇧🇪".
1. get_flag("BJ") should return "🇧🇯".
1. get_flag("BO") should return "🇧🇴".
1. get_flag("BA") should return "🇧🇦".
1. get_flag("BR") should return "🇧🇷".
1. get_flag("BG") should return "🇧🇬".
1. get_flag("CA") should return "🇨🇦".
1. get_flag("CL") should return "🇨🇱".
1. get_flag("CN") should return "🇨🇳".
1. get_flag("CO") should return "🇨🇴".
1. get_flag("HR") should return "🇭🇷".
1. get_flag("CY") should return "🇨🇾".
1. get_flag("CZ") should return "🇨🇿".
1. get_flag("DK") should return "🇩🇰".
1. get_flag("EC") should return "🇪🇨".
1. get_flag("ER") should return "🇪🇷".
1. get_flag("EE") should return "🇪🇪".
1. get_flag("FI") should return "🇫🇮".
1. get_flag("FR") should return "🇫🇷".
1. get_flag("GE") should return "🇬🇪".
1. get_flag("DE") should return "🇩🇪".
1. get_flag("GB") should return "🇬🇧".
1. get_flag("GR") should return "🇬🇷".
1. get_flag("GW") should return "🇬🇼".
1. get_flag("HT") should return "🇭🇹".
1. get_flag("HK") should return "🇭🇰".
1. get_flag("HU") should return "🇭🇺".
1. get_flag("IS") should return "🇮🇸".
1. get_flag("IN") should return "🇮🇳".
1. get_flag("IR") should return "🇮🇷".
1. get_flag("IE") should return "🇮🇪".
1. get_flag("IL") should return "🇮🇱".
1. get_flag("IT") should return "🇮🇹".
1. get_flag("JM") should return "🇯🇲".
1. get_flag("JP") should return "🇯🇵".
1. get_flag("KZ") should return "🇰🇿".
1. get_flag("KE") should return "🇰🇪".
1. get_flag("XK") should return "🇽🇰".
1. get_flag("KG") should return "🇰🇬".
1. get_flag("LV") should return "🇱🇻".
1. get_flag("LB") should return "🇱🇧".
1. get_flag("LI") should return "🇱🇮".
1. get_flag("LT") should return "🇱🇹".
1. get_flag("LU") should return "🇱🇺".
1. get_flag("MG") should return "🇲🇬".
1. get_flag("MY") should return "🇲🇾".
1. get_flag("MT") should return "🇲🇹".
1. get_flag("MX") should return "🇲🇽".
1. get_flag("MD") should return "🇲🇩".
1. get_flag("MC") should return "🇲🇨".
1. get_flag("MN") should return "🇲🇳".
1. get_flag("ME") should return "🇲🇪".
1. get_flag("MA") should return "🇲🇦".
1. get_flag("NL") should return "🇳🇱".
1. get_flag("NZ") should return "🇳🇿".
1. get_flag("NG") should return "🇳🇬".
1. get_flag("MK") should return "🇲🇰".
1. get_flag("NO") should return "🇳🇴".
1. get_flag("PK") should return "🇵🇰".
1. get_flag("PH") should return "🇵🇭".
1. get_flag("PL") should return "🇵🇱".
1. get_flag("PT") should return "🇵🇹".
1. get_flag("PR") should return "🇵🇷".
1. get_flag("RO") should return "🇷🇴".
1. get_flag("SM") should return "🇸🇲".
1. get_flag("SA") should return "🇸🇦".
1. get_flag("RS") should return "🇷🇸".
1. get_flag("SG") should return "🇸🇬".
1. get_flag("SK") should return "🇸🇰".
1. get_flag("SI") should return "🇸🇮".
1. get_flag("ZA") should return "🇿🇦".
1. get_flag("KR") should return "🇰🇷".
1. get_flag("ES") should return "🇪🇸".
1. get_flag("SE") should return "🇸🇪".
1. get_flag("CH") should return "🇨🇭".
1. get_flag("TH") should return "🇹🇭".
1. get_flag("TT") should return "🇹🇹".
1. get_flag("TR") should return "🇹🇷".
1. get_flag("UA") should return "🇺🇦".
1. get_flag("AE") should return "🇦🇪".
1. get_flag("US") should return "🇺🇸".
1. get_flag("UY") should return "🇺🇾".
1. get_flag("UZ") should return "🇺🇿".
1. get_flag("VE") should return "🇻🇪".
