import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

# Set a string variable to use 
line1 = "Hello World!\nWe can write anything we want here using Python"

# Launch a dialog box in kodi showing the string variable 'line1' as the contents
xbmcgui.Dialog().ok(addonname, line1)
