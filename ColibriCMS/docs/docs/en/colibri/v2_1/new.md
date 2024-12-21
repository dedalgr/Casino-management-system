# Revision 220

Date: 21.10.2020

* Added relay response time
* Minimum rfid scan value from 100 to 1
* Corrected class for registration of POS terminal from place
* Correction of gaps with a negative sign
* Fixed direct printing of windows

# Revision 221

Date: 22.10.2020

* Repaired relay test button
* Correct the size of digital fields
* Change the schedule

# Revision 223

Date: 23.10.2020

* Repair real-time monitoring

# Revision 227

Date: 26.10.2020

* Opens a second communication port

    SMIB controllers are attached to one and programs to the other
    
* Fixed client gluing with SMIB

# Revision 229

Date: 31.10.2020

* Fix in opening a missing reader
* Reports add graphics

# Revision 230

Date: 01.11.2020

* Monthly report without check for open shifts
* Repair user lock when closing a program

# Revision 231

Date: 04.11.2020

* Repair machine report

# Revision 237

Date: 05.11.2020

* Allowed hashout for the amount on the display
* Correction in absences
* Picture correction
* Prohibition to direct registration at POS Terminal

# Revision 238

Date: 12.11.2020

* Windows-based backup
* Window-based recovery
* Windows-based re-indexing

# Revision 239

Date: 13.11.2020

* Localization in English
* Repair by reading rfid

# Revision 240

Date: 16.11.2020

* Does not deduct mysteries in the absence of a climate card

# Revision 241

Date: 20.11.2020

* Repair loss of RFID reader
* Fix recording errors from the server
* The server cannot record an error with a level below WARNING

# Revision 242

Date: 22.11.2020

* Localization of the program
* Localization of templates

# Revision 243

Date: 24.11.2020

* Customer retention bonus, corrected croupier enrollment
* Book a machine for a client by date and time
* Allows stopping processes without consequences
* Corrects customer bonus withholding of the wrong user

# Revision 244

Date: 02.12.2020

* Access rights when loading a foreign user profile
* Repair not saved client to card
* Localization of SMIB
* Correction localization en
* Save machine changes to the jackpot server

# Revision 245

Date: 03.12.2020

* Fix logging level

# Revision 248

Date: 27.12.2020

* Fix VACUUM, reindex and revert DB

# Revision 249

Date: 03.03.2021

* Resize frame in jackpot settings 
* Fix in deleting log tables 
* Change APP password for gmail 

# Revision 250

Date: 03.03.2021

* Fix Gmail connections

# Revision 251

Date: 08.03.2021

* Edit report date
* Edit report number 

# Revision 252

Date: 09.03.2021

* Added reset machines in a daily report

# Revision 253

Date: 16.03.2021

* Fix order

# Revision 259

Date: 25.04.2021

* Added total detection for customer bonus based on the previous day 
* Added total detection for customer bonus on a monthly basis 
* Added redirect to client group based on total 
* Change in encryption. It is done with a random key
* Change the communication protocol from UDP to TCP 
* New template of daily and monthly reports adapted for the NRA 
* Add transfers to the cash order 
* Change the way to open a port to the base 
* Added option to ban a POS terminal (under development) 
* Change in base models 
* Fixed visualization reboot
* Added visualization shutdown 

# Revision 262

Date: 28.04.2021

* Run in windows 10 with last update

# Revision 264

Date: 29.04.2021

* Fix open PDF file on WINDOWS

# Revision 271

Date: 08.05.2021

* Fix in Crypt

# Revision 274

Date: 09.05.2021

* Added bet or credit bonus scroll

# Revision 275

Date: 12.05.2021

* Sync time zone

# Revision 276

Date: 13.05.2021

* Add repair row

# Revision 277

Date: 14.05.2021

* Fix time zone when start system

# Revision 285

Date: 20.05.2021

* Add in SMIB config N0x options (no use hex)
* Fix mony transfer.
* Fix commit
* reset player fix

# Revision 286

Date: 24.05.2021

* Fix wrong transfer mony
* Fix edit counter

# Revision 288

Date: 31.05.2021

* Fix in table absence
* Send an email from a list separated by ',' 

# Revision 293

Date: 03.06.2021

* Add max monyback
* Add Monybeck in user report
* Fix in send mail
* Resize colum by text in field
* Restricted client bonus
* Fix On Day Back Total. Get last cust coming date.

# Revision 314

Date: 23.06.2021

* Moved lock of bill from config file to database. Defined by a user group
* Moved auto mail from config to base. Defined by a user group
* Moved email for owner and service. Defined by a user group
* Moved email subject. Defined by a user group
* Moved Remove the entire bill. Defined by a user group
* Added encoding CP-1250 and CP-1252
* The program works with the server time zone.
* Changed group redirection with change in customer level, based on last total.
* Added restricted IN to the customer bonus
* Added restricted IN to the bonus card
* Repair in configuration file (accepts values ​​of all encoding)
* Possibility to set a direct customer bonus without waiting for entry
* Fixed documentation 
* Add primary accounting document in cashless
* Add primary accounting document in module clients 
* Print primary accounting document from day report 
* Fix RKO report time zone
* Add EIK field for company
* Try to unlock jackpot server if lost network from 3 to 5 times
* Fix in Minimal Revision
* Fix in direct print on windows
* Fix report by date
* Fix hold bonus
* Print on server with POS printer
* Show system time wit server timezone
* Fix text color
* Free RKO
* TCP protocol
* Fix error if edit mony.

# Revision 339

Date: 05.08.2021

* Fix in device cant get counter by SAS
* Add video on SMIB touch.
* Option to set rfid timeout to 0 on SMIB
* Save base bonus if redirect client group by total.
* Fix in Missing Mony
* Fix localization
* Fix red point 
* Set timeout to 0
* Check if the jackpot server is blocked
* Fix last edit time wit timezone
* Fix OnClose program if lost connection.
* All error in DB return last change by default.
* Fix bill get
* Fix SMIB log report
* Fix local

# Revision 343

Date: 16.08.2021

* Add bill report if edit order
* Add right "Edit hand order device"
* Add RKO report
* Print RKO copy
* Fix Bonus Hold
* Fix in missing mony
* Sort bonus report by datetime

# Revision 346

Date: 05.09.2021

* Customer bonus based on a percentage of the total

# Revision 351

Date: 05.09.2021

* Delete empty client groups 
* Fixed backup and restore based on windows 

# Revision 352

Date: 21.09.2021

* Fast RFID id add cust card
* Add SMIB blue skin

# Revision 364

Date: 13.10.2021

* Added database migration 
* Show redirected bonuses 
* Rounding of income and expenses 
* Fixed auto-update with minimal revision of windows
* Removed reference to SMIB log 
* SMIB WEB monitoring added to the service 

# Revision 367

Date: 22.11.2021

* Added client card copy without showing client settings 

# Revision 368

Date: 23.11.2021

* Duplicate group

# Revision 374

Date: 13.01.2022

* Write all IN/OUT in database
* Add field user in AFT IN/OUT report
* Fix round to 0.01 in AFT IN 
* Fix bonus for Impera. Is game is not selected transaction cannot be canceled.
* Displays the croupier's name on the daily and monthly reports
* Cash before report 
* Fix user edit. If have name raise error.

# Revision 375

Date: 15.01.2022

* Fix loging one option
* Fix jackpot user name and password

# Revision 382

Date: 08.02.2022

* Stop the tweeters of the bill adapters when reporting their release at the end of the shift
* Correction in the croupier's order regarding transfer income
* AFT fix on casino machines with ARM, added option to always submit the same transaction
* Remove email through local host
* Gmail is in cycle 3 of 10 minutes each
* Fixes Amatic startup communication with Windows
* Corrects forced manual reading when changing the machine number in the hall
* Fixes creating and removing users in the jackpot server
* Corrects customer bonus increments if not doubled
* Corrects an inscription for when a return is possible
* When returning by bet, it shows % instead of amount until the required bet is reached 
* DEBUG active new function for test
* Add EGN validator

# Revision 385

Date: 25.02.2022

* Djackpot by AFT
* Inventory of money 

# Revision 393

Date: 28.02.2022

* Autoconfig SAS

# Revision 402

Date: 09.03.2022

* From commit to flush
* User can crewate cust