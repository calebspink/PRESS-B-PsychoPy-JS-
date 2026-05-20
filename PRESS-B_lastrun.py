#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on April 22, 2026, at 15:31
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'sounddevice'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.1'
expName = 'Continuous Choice'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1920, 1080]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = './' + '%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\css0121\\Desktop\\PRESS-B\\PRESS-B_lastrun.py',
        savePickle=True, saveWideText=False,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('', )
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='fill',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'fill'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Welcome" ---
    # Run 'Begin Experiment' code from welcome_and_data_collection
    from psychopy import visual, core, event, data
    import pandas as pd
    
    #Initializes points
    points = 0
    
    #Created an Excel spreadsheet
    thisExp = data.ExperimentHandler(
        name='PRESS-B_test',
        extraInfo=expInfo,
        dataFileName=f"data/PRESS-B_{expInfo['participant']}/PRESS-B_{expInfo['participant']}"
    )
    #Reads file paths from CSV
    schedule_df = pd.read_csv('PRESS-B_Schedule_Entry.csv', na_values=['x']) #Reads CSV
    
    ding_path = schedule_df['Ding_Path'].iloc[0]
    womp_path = schedule_df['Womp_Path'].iloc[0]
    keyboard_path = schedule_df['Keyboard_Path'].iloc[0]
    
    #Initializes data for collection
    trialClock = core.Clock()
    session_number = []
    schedule = []
    bluePressTimes = []
    yellowPressTimes = []
    ctrlPressTimes = []
    point_earned = []
    responseTimes = []
    lastResponseTime = None
    
    #Tells the user how to begin the experiment
    welcome_message = visual.TextStim(win,
        text="Hello, thank you for participating in the experiment.\nIf you wish to stop participating, hit the 'Escape' key; however, you will not receive sona credit.\nHit 'Enter' when you are ready to begin.",
        height=0.05, color=[1,1,1], pos=[0, 0])
        
    #Shows welcome message, is a function for efficency
    def draw_welcome():
        welcome_message.draw()
        win.flip()
        
    
    
    # --- Initialize components for Routine "Trial" ---
    # Run 'Begin Experiment' code from omnicode
    #Do not delete this component
    
    #PsychoPy imports
    from psychopy import core, event, visual, monitors, sound
    
    #Python specific imports
    import time
    import pandas as pd
    
    #Replace random.random()
    def random_float(state=[None]):
        #Initialize state 
        if state[0] is None:
            state[0] = id(object())
        
        # Combine multiple sources of entropy
        seed = id(object()) + id([]) + id({}) + hash(str(id(object())))
        
        # Mix with previous state
        seed = seed ^ state[0]
        
        # Multiple rounds of mixing with different constants
        seed = (seed * 2654435761) % (2**32)
        seed = (seed ^ (seed >> 16)) * 0x85ebca6b
        seed = (seed ^ (seed >> 13)) * 0xc2b2ae35
        seed = seed ^ (seed >> 16)
        
        # Update state for next call
        state[0] = seed
        
        # Normalize to 0-1
        return (seed % 1000000007) / 1000000007
    
    def ln(x, tol=1e-9):
        """Natural logarithm using binary search with Taylor series exp"""
        if x <= 0:
            raise ValueError("ln undefined for x <= 0")
        if x == 1:
            return 0.0
        
        def exp_series(y):
            # Clamp y to avoid overflow/underflow
            if y > 50:
                return 1e50  # Very large number
            if y < -50:
                return 1e-50  # Very small number
            
            term = 1.0
            result = 1.0
            for n in range(1, 100):  # More iterations
                term *= y / n
                result += term
                if abs(term) < 1e-15:  # Better tolerance
                    break
            return result
        
        # Better initial bounds based on input
        if x < 1:
            low, high = -20.0, 0.0
        else:
            low, high = 0.0, 20.0
        
        # Binary search for ln(x)
        for _ in range(100):  # Limit iterations
            if high - low < tol:
                break
            mid = (low + high) / 2
            exp_mid = exp_series(mid)
            if exp_mid < x:
                low = mid
            else:
                high = mid
        
        return (low + high) / 2
    
    def log_base(x, base, tol=1e-9):
        """Logarithm with arbitrary base using the improved ln function"""
        if base <= 0 or base == 1:
            raise ValueError("Base must be positive and not equal to 1")
        return ln(x, tol) / ln(base, tol)
    
    #Replace np.random.normal()
    def random_normal(mu=0.0, sigma=1.0, state=[None]):
        """
        Generate normally distributed random numbers using Box-Muller transform.
        
        Args:
            mu: Mean of the normal distribution
            sigma: Standard deviation of the normal distribution
            state: State for the random_float function
        
        Returns:
            A random sample from N(mu, sigma^2)
        """
        # Helper functions
        def sqrt(x):
            if x == 0:
                return 0
            guess = x / 2.0
            for _ in range(20):
                guess = (guess + x / guess) / 2.0
            return guess
        
        def cos(x):
            # Taylor series for cos(x)
            x = x % (2 * 3.14159265359)
            result = 1.0
            term = 1.0
            for n in range(1, 30):
                term *= -x * x / ((2 * n - 1) * (2 * n))
                result += term
                if abs(term) < 1e-10:
                    break
            return result
        
        # Generate two uniform random numbers in (0, 1)
        u1 = random_float(state)
        u2 = random_float(state)
        
        # Ensure u1 is not zero (would cause log(0))
        while u1 == 0 or u1 == 1:
            u1 = random_float(state)
        
        # Box-Muller transform
        pi = 3.14159265359
        ln_u1 = ln(u1)
        z0 = sqrt(-2.0 * ln_u1) * cos(2.0 * pi * u2)
        
        # Scale and shift to desired mean and std dev
        return mu + sigma * z0
    
    def random_exponential(scale=1.0, state=[None]):
        """
        Generate exponentially distributed random numbers.
        
        The exponential distribution is often used for modeling time between events
        in a Poisson process (e.g., time between arrivals, lifetimes).
        
        Args:
            scale: The scale parameter (1/lambda), which is the mean of the distribution.
                   Note: np.random.exponential uses 'scale' (the mean), not 'rate' (lambda).
            state: State for the random_float function
        
        Returns:
            A random sample from Exponential(scale)
        """
        # Generate uniform random number in (0, 1)
        u = random_float(state)
        
        # Ensure u is not zero (would cause log(0))
        while u == 0 or u == 1:
            u = random_float(state)
        
        # Inverse transform: X = -scale * ln(U)
        return -scale * ln(u)
    
    #Replace np.random.permutation()
    def random_permutation(n, state=[None]):
        """
        Randomly permute a sequence or return a permuted range.
        
        Args:
            n: If an integer, returns a random permutation of range(n).
               If a sequence (list/tuple), returns a shuffled copy of it.
            state: State for the random_float function
        
        Returns:
            A randomly permuted array/list
        """
        # Handle integer input - create range
        if isinstance(n, int):
            arr = list(range(n))
        else:
            # Handle sequence input - make a copy
            arr = list(n)
        
        # Fisher-Yates shuffle algorithm
        for i in range(len(arr) - 1, 0, -1):
            # Generate random index from 0 to i (inclusive)
            j = int(random_float(state) * (i + 1))
            
            # Handle edge case where random_float returns exactly 1.0
            if j > i:
                j = i
            
            # Swap elements
            arr[i], arr[j] = arr[j], arr[i]
        
        return arr
    
    #Replace random.choice()
    def choice(sequence):    
        # Get random index
        random_index = int(random_float() * len(sequence))
        
        # Handle edge case where random_float returns exactly 1.0
        if random_index >= len(sequence):
            random_index = len(sequence) - 1
        
        return sequence[random_index]
        
    #Replace np.array.equal
    def check_colors(color1, color2):
        if len(color1) != len(color2):
            return False
        for i in range(len(color1)):
            if color1[i] != color2[i]:
                return False
        return True
        
    routine_clock = core.Clock()
    
    #Uses schedule data from the CSV as a DataFrame
    schedule_df = pd.read_csv('PRESS-B_Schedule_Entry.csv', na_values=['x']) #Reads CSV
    
    keyboard_path = schedule_df['Keyboard_Path'].iloc[0]
    
    #Grabs list of schedules
    schedule_df = schedule_df[~schedule_df['Schedule_number'].isin(['File_path_ding', 'File_path_womp'])]
    all_schedules = list(schedule_df['Schedule_number'])
    
    #Removes 'EXT', 'ACQ', and Tutorial from main trial block
    try:
        all_schedules.remove('EXT')
        all_schedules.remove('ACQ')
        all_schedules.remove('Tutorial')
        all_schedules.remove('Keyboard_Tutorial')
    #Program will still run if any or all are missing
    except ValueError:
        pass
    
    #Prints schedules for debugging. I strongly suggest keeping this.
    print(all_schedules)
    print(f"number of initial schedules: {len(all_schedules)}")
    #Initializes a list of used schedules
    used_schedules = []
    
    #Upon initialization:
    switch_enabled = True #the tab button works 
    tab_pressed = False #no changeover delay
    gl_flash = False #the reinforcement light does not flash
    rl_flash = False #the punishment light does not flash
    current_sound = None #no sound plays
    handle_blackout = False #no blackout period
    
    session_number = 0
    
    points = 0 #the subject starts with 0 points
        
    #Note:
    #These varibles are just initialized here.
    #They are actually set in the ScheduleManager() class.
    
    #Press indicies
    press_blue_earn_index = 0
    press_blue_loss_index = 0
    press_yellow_earn_index = 0
    press_yellow_loss_index = 0
    
    blue_fh_index = 0
    yellow_fh_index = 0
    blue_pun_fh_index = 0
    yellow_pun_fh_index = 0
    
    #Intializes proc values as impossible
    blue_earn_proc_value = 1
    blue_loss_proc_value = 1
    yellow_earn_proc_value = 1
    yellow_loss_proc_value = 1
    
    #Initializes proc values
    blue_interval_earn_value = random_float()
    yellow_interval_earn_value = random_float()
    blue_interval_loss_value = random_float()
    yellow_interval_loss_value = random_float()
    
    #Light colors
    light_on = [1, 1, 1] #White
    light_off = [-1, -1, -1] #Black
    button_color1 = [-1, -1, 1] #Blue
    button_color2 = [1, 1, -1] #Yellow
    
    light_state = "OFF"
    
    context_cache = {}
    
    #Objects
    green_light = visual.Rect(win, 
        width=0.2, height=0.2, 
        fillColor=[-1.0000, -0.3020, -1.0000], 
        colorSpace='rgb', pos=[-0.45, 0])
        
    red_light = visual.Rect(win,
        width=0.2, height=0.2,
        fillColor=[-0.3020, -1, -1.0000],
        colorSpace='rgb', pos=[0.45,0])
        
    button_response = visual.Rect(win, 
        width=0.65, height=0.4, 
        fillColor=[-1, -1, 1], lineColor=[0,0,0], 
        colorSpace='rgb', pos=[0, 0],
        opacity=1)
        
    button_cycle = visual.Rect(win, 
        width=0.65, height=0.1, 
        fillColor=[0.6549,0.6549,0.6549], 
        lineColor=[0,0,0], colorSpace='rgb', 
        pos=[0,-0.3], opacity=1)
        
    switch_text = visual.TextStim(win, 
        text='SWITCH', height=0.05, 
        color=[-1,-1,-1], pos=[0,-0.3],
        opacity=1)
        
    points_display = visual.TextStim(win, 
        text='Points: 0', height=0.05,
        color=[-1,-1,-1], pos=[0,0.25])
        
    light_1 = visual.Rect(win, 
        width=0.125, height=0.125, 
        fillColor=light_off, 
        colorSpace='rgb',
        pos=[(-0.75, 0.4)])
        
    light_2 = visual.Rect(win, 
        width=0.125, height=0.125, 
        fillColor=light_off, 
        colorSpace='rgb', 
        pos=[(-0.60, 0.4)])
        
    light_3 = visual.Rect(win, 
        width=0.125, height=0.125, 
        fillColor=light_off, 
        colorSpace='rgb',
        pos=[(-0.45, 0.4)])
    
    light_4 = visual.Rect(win, 
        width=0.125, height=0.125, 
        fillColor=light_off, 
        colorSpace='rgb',
        pos=[(-0.3, 0.4)])
    
    light_5 = visual.Rect(win, 
        width=0.125, height=0.125, 
        fillColor=light_off, 
        colorSpace='rgb', 
        pos=[(-0.15, 0.4)])
        
    light_6 = visual.Rect(win, 
        width=0.125, height=0.125, 
        fillColor=light_off, 
        colorSpace='rgb', 
        pos=[(0, 0.4)])
        
    light_7 = visual.Rect(win, 
        width=0.125, height=0.125, 
        fillColor=light_off, 
        colorSpace='rgb', 
        pos=[(0.15, 0.4)])
        
    light_8 = visual.Rect(win, 
        width=0.125, height=0.125, 
        fillColor=light_off, 
        colorSpace='rgb',
        pos=[(0.3, 0.4)])
        
    light_9 = visual.Rect(win, 
        width=0.125, height=0.125, 
        fillColor=light_off, 
        colorSpace='rgb', 
        pos=[(0.45, 0.4)])
        
    light_10 = visual.Rect(win, 
        width=0.125, height=0.125, 
        fillColor=light_off, 
        colorSpace='rgb',
        pos=[(0.6, 0.4)])
        
    light_11 = visual.Rect(win, 
        width=0.125, height=0.125, 
        fillColor=light_off, 
        colorSpace='rgb',
        pos=[(0.75, 0.4)])
    
    #'bo' is short for "Blackout"
    response_bo = visual.Rect(win,
        height=0.4, width=0.65,
        fillColor=[0.6549, 0.6549, 0.6549],
        pos=(0,0), colorSpace='rgb')
    
    timer_text = visual.TextStim(win,
        text="Time Remaining: 15",
        pos=(0,0), height=0.05, color='black')
    
    green_light_bo = visual.Rect(win, 
        width=0.2, height=0.2, 
        fillColor=[0.3339, 0.3339, 0.3339], 
        colorSpace='rgb', pos=[-0.45, 0])
    
    red_light_bo = visual.Rect(win,
        width=0.2, height=0.2,
        fillColor=[0.3339, 0.3339, 0.3339],
        colorSpace='rgb', pos=[0.45,0])
    
    button_cycle_bo = visual.Rect(win, 
        width=0.65, height=0.1, 
        fillColor=[0.4549,0.4549,0.4549], 
        lineColor=[0,0,0], colorSpace='rgb', 
        pos=[0,-0.3])
    
    points_display = visual.TextStim(win, 
        text='Points: 0', height=0.05,
        color=[-1,-1,-1], pos=[0,0.25]) 
    
    #Dictionary of lights
    light_mapping = {
        1: light_1, 2: light_2, 3: light_3,
        4: light_4, 5: light_5, 6: light_6,
        7: light_7, 8: light_8, 9: light_9, 
        10: light_10, 11: light_11
    }
    
    lights = [light_1, light_2, light_3, 
                light_4, light_5, light_6,
                light_7, light_8, light_9,
                light_10, light_11]
    
    def reset_routine_clock():
        routine_clock.reset()
    
    class ScheduleManager:
        def __init__(self, blue_i, yellow_i, blue_pun_i, yellow_pun_i, 
                     blue_r, yellow_r, blue_pun_r, yellow_pun_r,
                     blue_random_r, yellow_random_r,
                     blue_pun_random_r, yellow_pun_random_r,
                     blue_random_i, yellow_random_i,
                     blue_pun_random_i, yellow_pun_random_i,
                     blue_fh, yellow_fh, blue_pun_fh, yellow_pun_fh, 
                     blue_fh_n_intervals, yellow_fh_n_intervals, 
                     blue_pun_fh_n_intervals, yellow_pun_fh_n_intervals, 
                     blue_fh_type, yellow_fh_type, blue_pun_fh_type, 
                     yellow_pun_fh_type, session_duration, blue_mag, yellow_mag, 
                     blue_pun_mag, yellow_pun_mag, changeover_delay, 
                     blackout_duration, blue_dist_type, yellow_dist_type,
                     blue_pun_dist_type, yellow_pun_dist_type,
                     sd_blue_interval, sd_yellow_interval, 
                     sd_blue_pun_interval, sd_yellow_pun_interval, 
                     schedule_lights, context_path, context_position,
                     context_size, context_opacity, context_depth,
                     ding_path, womp_path):
            
            # Initialize reinforcement and punishment parameters
            self.blue_i = blue_i or float('inf')
            self.yellow_i = yellow_i or float('inf')
            self.blue_pun_i = blue_pun_i or float('inf')
            self.yellow_pun_i = yellow_pun_i or float('inf')
    
            self.blue_r = blue_r or float('inf')
            self.yellow_r = yellow_r or float('inf')
            self.blue_pun_r = blue_pun_r or float('inf')
            self.yellow_pun_r = yellow_pun_r or float('inf')
            
            self.blue_random_r = blue_random_r or -float('inf')
            self.yellow_random_r = yellow_random_r or -float('inf')
            self.blue_pun_random_r = blue_pun_random_r or -float('inf')
            self.yellow_pun_random_r = yellow_pun_random_r or -float('inf')
            
            """
            Not using these
            # Random ratio probabilities
            if self.blue_random_r != -float('inf'):
                self.blue_random_r_chance = 1/self.blue_random_r
            else:
                self.blue_random_r_chance = -float('inf')
        
            if self.yellow_random_r != -float('inf'):
                self.yellow_random_r_chance = 1/self.yellow_random_r
            else:
                self.yellow_random_r_chance = -float('inf')
    
            if self.blue_pun_random_r != -float('inf'):
                self.blue_pun_random_r_chance = 1/self.blue_pun_random_r
            else:
                self.blue_pun_random_r_chance = -float('inf')
    
            if self.yellow_pun_random_r != -float('inf'):
                self.yellow_pun_random_r_chance = 1/self.yellow_pun_random_r
            else:
                self.yellow_pun_random_r_chance = -float('inf')
            """
            
            self.blue_random_i = blue_random_i or float('inf')
            self.yellow_random_i = yellow_random_i or float('inf')
            self.blue_pun_random_i = blue_pun_random_i or float('inf')
            self.yellow_pun_random_i = yellow_pun_random_i or float('inf')
            
            """
            We are not using these rn.
            # Random interval probabilities
            if self.blue_random_i != -float('inf'):
                self.blue_random_i_chance = 1/self.blue_random_i
            else:
                self.blue_random_i_chance = -float('inf')
        
            if self.yellow_random_i != -float('inf'):
                self.yellow_random_i_chance = 1/self.yellow_random_i
            else:
                self.yellow_random_i_chance = -float('inf')
    
            if self.blue_pun_random_i != -float('inf'):
                self.blue_pun_random_i_chance = 1/self.blue_pun_random_i
            else:
                self.blue_pun_random_i_chance = -float('inf')
    
            if self.yellow_pun_random_i != -float('inf'):
                self.yellow_pun_random_i_chance = 1/self.yellow_pun_random_i
            else:
                self.yellow_pun_random_i_chance = -float('inf')
            """
            
            #Distribution type 
            self.blue_dist_type = blue_dist_type
            self.yellow_dist_type = yellow_dist_type
            self.blue_pun_dist_type = blue_pun_dist_type
            self.yellow_pun_dist_type = yellow_pun_dist_type
    
            # Fleshler-Hoffman configuration
            self.blue_fh = blue_fh or False
            self.yellow_fh = yellow_fh or False
            self.blue_pun_fh = blue_pun_fh or False
            self.yellow_pun_fh = yellow_pun_fh or False
    
            self.blue_fh_n_intervals = blue_fh_n_intervals or 0
            self.yellow_fh_n_intervals = yellow_fh_n_intervals or 0
            self.blue_pun_fh_n_intervals = blue_pun_fh_n_intervals or 0
            self.yellow_pun_fh_n_intervals = yellow_pun_fh_n_intervals or 0
    
            self.blue_fh_type = blue_fh_type or False
            self.yellow_fh_type = yellow_fh_type or False
            self.blue_pun_fh_type = blue_pun_fh_type or False
            self.yellow_pun_fh_type = yellow_pun_fh_type or False
            
            self.blue_earn_last_update = core.getTime()
            self.yellow_earn_last_update = core.getTime()
            self.blue_loss_last_update = core.getTime()
            self.yellow_loss_last_update = core.getTime()
            
            self.blue_ratio_earn_value = random_float()
            self.yellow_ratio_earn_value = random_float()
            self.blue_pun_ratio_earn_value = random_float()
            self.yellow_pun_ratio_earn_value = random_float()
            
            self.blue_interval_earn_value = random_float()
            self.yellow_interval_earn_value = random_float()
            self.blue_interval_loss_value = random_float()
            self.yellow_interval_loss_value = random_float()
    
            # Indices for sequence tracking
            self.blue_fh_index = 0
            self.yellow_fh_index = 0
            self.blue_pun_fh_index = 0
            self.yellow_pun_fh_index = 0
            
            self.blue_fh_values = []
            self.yellow_fh_values = []
            self.blue_pun_fh_values = []
            self.yellow_pun_fh_values = []
            
            self.blue_fh_list = []
            self.yellow_fh_list = []
            self.blue_pun_fh_list = []
            self.yellow_pun_fh_list = []
            
            #Context images
            self.context_path = context_path or None
            self.context_position = context_position or (0,0) #Default in center
            self.context_size = context_size or [2,2] #Default whole screen
            self.context_opacity = context_opacity or None #Default opaque
            self.context_depth = context_depth or -1 #Default background
             
            self.ding_path = ding_path or None
            self.womp_path = womp_path or None
             
            self.generate_fleshler_hoffman_list()
                 
            # General configuration
            self.session_duration = session_duration
            self.blue_mag = blue_mag or 0
            self.yellow_mag = yellow_mag or 0
            self.blue_pun_mag = blue_pun_mag or 0
            self.yellow_pun_mag = yellow_pun_mag or 0
            self.changeover_delay = changeover_delay or 0
            self.blackout_duration = blackout_duration or 0
            self.sd_blue_interval = sd_blue_interval or 0
            self.sd_yellow_interval = sd_yellow_interval or 0
            self.sd_blue_pun_interval = sd_blue_pun_interval or 0
            self.sd_yellow_pun_interval = sd_yellow_pun_interval or 0
            
            self.schedule_lights = schedule_lights or "OFF"
            
            self.next_blue_earn_time = 0
            self.next_blue_loss_time = 0
            self.next_yellow_earn_time = 0
            self.next_yellow_loss_time = 0
            
            self.current_interval_time = 0 
            
            self.last_switch_time = 0
            self.interval_start = routine_clock.getTime()
            self.reset_times()
        
        def calculate_fleshler_hoffman(self, mean, n_intervals):
            
            #Define e here to avoid human and machine confusion
            e = 2.718281828 
            
            if mean is None or n_intervals is None or n_intervals <= 0:
                return [0]
            n_intervals = int(n_intervals)
            intervals = []
            for n in range(1, n_intervals + 1):
                if n == n_intervals:
                    tn = mean * (1 + log_base(n_intervals, e))
                else:
                    tn = mean * (1 + log_base(n_intervals, e) +
                                 (n_intervals - n) * log_base(n_intervals - n, e) -
                                 (n_intervals - n + 1) * log_base(n_intervals - n + 1, e))
                intervals.append(tn)
            return intervals
            
        def generate_fleshler_hoffman_list(self):
            def process_fh_list(fh_flag, i_value, r_value, n_intervals, fh_type):
                if not fh_flag:
                    return [float('inf')]
            
                value = i_value if i_value > 0 and i_value != float('inf') else r_value
                if value <= 0 or value == float('inf'):
                    return [float('inf')]
            
                fh_values = self.calculate_fleshler_hoffman(value, n_intervals)
            
                try:
                    if fh_type.upper() == "PROGRESSIVE":
                        return sorted(fh_values)
                    elif fh_type.upper() == "REGRESSIVE":
                        return sorted(fh_values, reverse=True)
                    elif fh_type.upper() == "RANDOM":
                        return random_permutation(fh_values)
                    else:
                        raise ValueError(f"Invalid FH type: {fh_type}")
                except Exception as e:
                    print(f"Error processing Fleshler-Hoffman list: {e}")
                    return [float('inf')]
    
            self.blue_fh_list = process_fh_list(
                self.blue_fh, self.blue_i, self.blue_r, 
                self.blue_fh_n_intervals, self.blue_fh_type
            )
    
            self.yellow_fh_list = process_fh_list(
                self.yellow_fh, self.yellow_i, self.yellow_r, 
                self.yellow_fh_n_intervals, self.yellow_fh_type
            )
    
            self.blue_pun_fh_list = process_fh_list(
                self.blue_pun_fh, self.blue_pun_i, self.blue_pun_r, 
                self.blue_pun_fh_n_intervals, self.blue_pun_fh_type
            )
    
            self.yellow_pun_fh_list = process_fh_list(
                self.yellow_pun_fh, self.yellow_pun_i, self.yellow_pun_r, 
                self.yellow_pun_fh_n_intervals, self.yellow_pun_fh_type
            )
            
        def calculate_next_blue_earn_time(self, button_response):
            """Determines the next reinforcement time for blue VI schedules."""
            if self.blue_fh and self.blue_i > 0 and self.blue_i != float('inf'):
                interval = self.blue_fh_list[self.blue_fh_index]
                self.blue_fh_index = (self.blue_fh_index + 1) % len(self.blue_fh_list)
            else:
                if self.blue_dist_type == "GAUSSIAN":
                    interval = max(random_normal(self.blue_random_i, self.sd_blue_interval), 0)
                else:
                    interval = random_exponential(scale=self.blue_random_i)
            return routine_clock.getTime() + interval
        
        def calculate_next_yellow_earn_time(self, button_response):
            """Determines the next reinforcement time for yellow VI schedules."""
            if self.yellow_fh and self.yellow_i > 0 and self.yellow_i != float('inf'):
                interval = self.yellow_fh_list[self.yellow_fh_index]
                self.yellow_fh_index = (self.yellow_fh_index + 1) % len(self.yellow_fh_list)
            else:
                if self.yellow_dist_type == "GAUSSIAN":
                    interval = max(random_normal(self.yellow_random_i, self.sd_yellow_interval), 0)
                else:
                    interval = random_exponential(scale=self.yellow_random_i)
            return routine_clock.getTime() + interval
        
        def calculate_next_blue_loss_time(self, button_response):
            """Determines the next punishment time for blue VI schedules."""
            if self.blue_pun_fh and self.blue_pun_i > 0 and self.blue_pun_i != float('inf'):
                interval = self.blue_pun_fh_list[self.blue_pun_fh_index]
                self.blue_pun_fh_index = (self.blue_pun_fh_index + 1) % len(self.blue_pun_fh_list)
            else:
                if self.blue_pun_dist_type == "GAUSSIAN":
                    interval = max(random_normal(self.blue_pun_random_i, self.sd_blue_pun_interval), 0)
                else:
                    interval = random_exponential(scale=self.blue_pun_random_i)
            return routine_clock.getTime() + interval
        
        def calculate_next_yellow_loss_time(self, button_response):
            """Determines the next punishment time for yellow VI schedules."""
            if self.yellow_pun_fh and self.yellow_pun_i > 0 and self.yellow_pun_i != float('inf'):
                interval = self.yellow_pun_fh_list[self.yellow_pun_fh_index]
                self.yellow_pun_fh_index = (self.yellow_pun_fh_index + 1) % len(self.yellow_pun_fh_list)
            else:
                if self.yellow_pun_dist_type == "GAUSSIAN":
                    interval = max(random_normal(self.yellow_pun_random_i, self.sd_yellow_pun_interval), 0)
                else:
                    interval = random_exponential(scale=self.yellow_pun_random_i)
            return routine_clock.getTime() + interval
    
        def calculate_next_press_earn_requirement(self, button_response):
            if check_colors(button_response.fillColor, button_color1) == True:  # Blue
                if self.blue_fh and self.blue_r > 0 and self.blue_r != float('inf'):
                    interval = self.blue_fh_list[self.blue_fh_index]
                    self.blue_fh_index = (self.blue_fh_index + 1) % len(self.blue_fh_list)
                else:
                    if self.blue_dist_type == "GAUSSIAN":
                        interval = max(random_normal(self.blue_random_r, self.sd_blue_interval), 0)
                    else:
                        interval = random_exponential(scale=self.blue_random_r)
    
            elif check_colors(button_response.fillColor, button_color2) == False:  # Yellow
                if self.yellow_fh and self.yellow_r > 0 and self.yellow_r != float('inf'):
                    interval = self.yellow_fh_list[self.yellow_fh_index]
                    self.yellow_fh_index = (self.yellow_fh_index + 1) % len(self.yellow_fh_list)
                else:
                    if self.yellow_dist_type == "GAUSSIAN":
                        interval = max(random_normal(self.yellow_random_r, self.sd_yellow_interval), 0)
                    else:
                        interval = random_exponential(scale=self.yellow_random_r)
    
            else:
                interval = float('inf')
    
            return max(interval, 0)
            
        def calculate_next_press_loss_requirement(self, button_response):
            if check_colors(button_response.fillColor, button_color1) == True:  # Blue
                if self.blue_pun_fh and self.blue_pun_r > 0 and self.blue_pun_r != float('inf'):
                    interval = self.blue_pun_fh_list[self.blue_pun_fh_index]
                    self.blue_pun_fh_index = (self.blue_pun_fh_index + 1) % len(self.blue_pun_fh_list)
                else:
                    if self.blue_pun_dist_type == "GAUSSIAN":
                        interval = max(random_normal(self.blue_pun_random_r, self.sd_blue_pun_interval), 0)
                    else:
                        interval = random_exponential(scale=self.blue_pun_random_r)
    
            elif check_colors(button_response.fillColor, button_color2) == False:  # Yellow
                if self.yellow_pun_fh and self.yellow_pun_r > 0 and self.yellow_pun_r != float('inf'):
                    interval = self.yellow_pun_fh_list[self.yellow_pun_fh_index]
                    self.yellow_pun_fh_index = (self.yellow_pun_fh_index + 1) % len(self.yellow_pun_fh_list)
                else:
                    if self.yellow_pun_dist_type == "GAUSSIAN":
                        interval = max(random_normal(self.yellow_pun_random_r, self.sd_yellow_pun_interval), 0)
                    else:
                        interval = random_exponential(scale=self.yellow_pun_random_r)
    
            else:
                interval = float('inf')
    
            return max(interval, 0)
    
        #Updates earn intervals
        def update_earn_intervals(self, button_response):
            
            #Sets the next earn requirement for I and R schedules (bar RR)
    
            #Parameters
            #----------
            #button_response : object
                #The response button.
            
            if (button_response.fillColor == button_color1).all():  # Blue button
                self.next_blue_earn_time = routine_clock.getTime() + self.get_normal_interval_blue(self.blue_i)
                self.next_press_earn_requirement = self.calculate_next_press_earn_requirement(button_response)
            else:  # Yellow button
                self.next_yellow_earn_time = routine_clock.getTime() + self.get_normal_interval_yellow(self.yellow_i)
                self.next_press_earn_requirement = self.calculate_next_press_earn_requirement(button_response)
            
            if self.next_press_earn_requirement != float('inf'):
                self.rounded_next_earn_requirement = round(self.next_press_earn_requirement)
            else:
                self.rounded_next_earn_requirement = float('inf')
            
        def update_loss_intervals(self, button_response):
            
            #Sets the next earn time for FI and VI schedules
    
            #Parameters
            #----------
            #button_response : object
                #The response button.
            
            if (button_response.fillColor == button_color1).all():
                self.next_blue_loss_time = routine_clock.getTime() + self.get_normal_interval_blue_pun(self.blue_pun_i)
                self.next_press_loss_requirement = self.calculate_next_press_loss_requirement(button_response)
            else:
                self.next_yellow_loss_time = routine_clock.getTime() + self.get_normal_interval_yellow_pun(self.yellow_pun_i)
                self.next_press_loss_requirement = self.calculate_next_press_loss_requirement(button_response)
            
            if self.next_press_loss_requirement != float('inf'):
                self.rounded_next_loss_requirement = round(self.next_press_loss_requirement)
            else:
                self.rounded_next_loss_requirement = float('inf')
    
            #Generates the next earn condition for I and R schedules.
            #This is separate from FH intervals.
            #Each possiblity is its own function. (Trust me, it's easier this way)
    
            #Parameters
            #----------
            #mean_interval : float
                #The mean interval.
    
            #Returns
            #-------
            #float
                #A normally distributed interval value.
            
        def get_interval_blue(self, mean_interval):
            if self.blue_dist_type == "GAUSSIAN":
                return max(random_normal(loc=mean_interval, scale=self.sd_blue_interval), 0)
            else:
                return random_exponential(scale=mean_interval)
    
        def get_interval_yellow(self, mean_interval):
            if self.yellow_dist_type == "GAUSSIAN":
                return max(random_normal(loc=mean_interval, scale=self.sd_yellow_interval), 0)
            else:
                return random_exponential(scale=mean_interval)
    
        def get_interval_blue_pun(self, mean_interval):
            if self.blue_pun_dist_type == "GAUSSIAN":
                return max(random_normal(loc=mean_interval, scale=self.sd_blue_pun_interval), 0)
            else:
                return random_exponential(scale=mean_interval)
    
        def get_interval_yellow_pun(self, mean_interval):
            if self.yellow_pun_dist_type == "GAUSSIAN":
                return max(random_normal(loc=mean_interval, scale=self.sd_yellow_pun_interval), 0)
            else:
                return random_exponential(scale=mean_interval)
            
        def generate_one_second_interval(self):
    
            #Generate new interval values if one second has passed.
            #Exclusively for RI schedules. 
    
            self.current_interval_time = routine_clock.getTime()
            # Check if one second has passed
            if self.current_interval_time - self.interval_start >= 1:
            # Update interval values based on probabilities
                if self.blue_random_i > 0:
                    self.blue_interval_earn_value = random_float()
                if self.yellow_random_i > 0:
                    self.yellow_interval_earn_value = random_float()
                if self.blue_pun_random_i > 0:
                    self.blue_interval_loss_value = random_float()
                if self.yellow_pun_random_i > 0:
                    self.yellow_interval_loss_value = random_float()
                # Reset the interval start time
                self.interval_start = self.current_interval_time
    
        def reset_times(self):
            reset_routine_clock()
            self.current_interval_time = routine_clock.getTime()
            self.next_blue_earn_time = self.calculate_next_blue_earn_time(button_response)
            self.next_blue_loss_time = self.calculate_next_blue_loss_time(button_response)
            self.next_yellow_earn_time = self.calculate_next_yellow_earn_time(button_response)
            self.next_yellow_loss_time = self.calculate_next_yellow_loss_time(button_response)
            self.next_press_earn_requirement = self.calculate_next_press_earn_requirement(button_response)
            self.next_press_loss_requirement = self.calculate_next_press_loss_requirement(button_response)
            if self.next_press_earn_requirement != float('inf'):  
                self.rounded_next_earn_requirement = round(self.next_press_earn_requirement)
            else:
                self.rounded_next_earn_requirement = float('inf')
            if self.next_press_loss_requirement != float('inf'):    
                self.rounded_next_loss_requirement = round(self.next_press_loss_requirement)
            else:
                self.rounded_next_loss_requirement = float('inf')
                
    class FlashManager:
        
        #Class that handles the flashing of non-schedule lights.
        #Includes the green and red lights,the response and cycle buttons,
        #and changeover delay.
        
        #'gl' = green_light, 'rl' = red_light,
        #'rb' = button_response, 'cycle' = button_cycle
        #'switch_cod' = changeover delay
        
        def __init__(self):
            #Initializes flash states as 'False'
            self.flash_states = {'gl': False, 'rl': False, 
                                'switch_cod': False, 'rb': False, 
                                'cycle': False}
            #Flash times start times are at '0'
            self.flash_start_times = {'gl': 0, 'rl': 0, 
                                     'switch_cod': 0, 'rb': 0,
                                     'cycle': 0}
            #Duration of flashes, all values are in seconds
            self.flash_durations = {'gl': 0.25, 'rl': 0.25, 
                                    'switch_cod': 0.5, 'rb': 0.1,
                                    'cycle': 0.1} 
            #sets the orginial colors as None, that is [0, 0, 0]
            self.original_colors = {'rb': None, 'cycle': None}
    
        
        #Sets the appropriate flash type to 'True'.
        #This is called in other functions.
        
        #Parameters
        #----------
        #flash_type: string
            #Refers to which object should flash
            
        #start_time: integer
            #Makes sure the flashes start at 0. 
            
        #Returns
        #-------
        #None
        
        def start_flash(self, flash_type, start_time, object=None):
            self.flash_states[flash_type] = True
            self.flash_start_times[flash_type] = start_time
            if flash_type in ['rb', 'cycle'] and object is not None:
                self.original_colors[flash_type] = object.fillColor
                
        
        #Summary
        #Updates the flash state depending upon time.
        #If time between the start of the flash and current time
        #is less than flash duration, the object will stay its flash color.
        #If the elapsed time is greater than flash duration,
        #objects will return to their original color.
        
        #Parameters
        #----------
        #current_time: float
            #Current time in the routine
        #green_light: object
            #Reinforcement light
        #red_light: object
            #Punishment light
        #button_response: object
            #The response button.
        #button_cycle: object
            #Button that changes the response button color
            
        #Returns
            #None
    
        def update_flashes(self, current_time, green_light,
                            red_light, button_response, button_cycle):
            for flash_type in self.flash_states.keys():
                if self.flash_states[flash_type]:
                    if (current_time - self.flash_start_times[flash_type]) < self.flash_durations[flash_type]:
                        if flash_type == 'gl' and green_light is not None:
                            green_light.fillColor = [0.1294, 0.8667, 0.1294] #Flashes to a lime green
                        elif flash_type == 'rl' and red_light is not None:
                            red_light.fillColor = [0.8667, 0.1294, 0.1294] #Flashes to a salmon pink
                        elif flash_type == 'rb' and button_response is not None:
                            button_response.lineColor = button_response.fillColor #Object border will temporarily change to match .fillColor
                        elif flash_type == 'cycle' and button_cycle is not None:
                            button_cycle.fillColor = [0.8549, 0.8549, 0.8549] #Flashes a lighter gray
                    else: #Returns to original colors
                        self.flash_states[flash_type] = False
                        if flash_type == 'gl' and green_light is not None:
                            green_light.fillColor = [-1.0000, -0.3020, -1.0000]
                        elif flash_type == 'rl' and red_light is not None:
                            red_light.fillColor = [-0.3020, -1.0000, -1.0000]
                        elif flash_type == 'rb' and button_response is not None:
                            button_response.lineColor = [0, 0, 0]
                        elif flash_type == 'cycle' and button_cycle is not None:
                            button_cycle.fillColor = [0.6549, 0.6549, 0.6549]
    
    
    #Retrieves a new schedule from available schedules
    
    #Parameters
    #__________
    #None
    
    #Returns
    #-------
    #selected_schedule: string
        #The schedule that is selected.
        
    #None: None
        #If there are no available schedules, then None is returned.
    
    def get_new_schedule():
        available_schedules = list(set(all_schedules) - set(used_schedules))
        if len(available_schedules) > 0:
            if Selection_type.method=='random':
                selected_schedule = choice(available_schedules) #Pseudorandom selection on an available schedule
            else:
                available_schedules.sort()
                selected_schedule = available_schedules[0]
            used_schedules.append(selected_schedule) #Choosen schedule is added to used_schedules
            return selected_schedule
        else: #If there are no available schedules, then it will return None
            return None
            
    #Plays sounds
    
    #Parameters:
        #sound_obj: object
            #Sounds to be played
        #current_sound: object
            #Sets a sound, initialized as None
    
    #Returns:
        #object:
            #sound_obj, sound to be played
    
    def play_sound(sound_obj, current_sound=None):
        if current_sound is not None and current_sound.status == sound.STARTED:
            current_sound.stop() 
        sound_obj.play()
        return sound_obj
    
    #Logic for space key. Contains a list of conditions for
    #earning or losing a point.
    
    #Parameters:
        #t: float
            #Current time
        #schedule_manager: class
            #Handles the importation of schedule data
        #flash_manager: class
            #Handles flashes
        #points: integer
            #How many points the participant has earn
        #button_response: object
            #The response button
        #press_blue_earn_index: integer
            #How many times the buttone has been pressed
            #while blue until reinforced for blue presses
        #press_blue_loss_index: integer
            #How many times the buttone has been pressed
            #while blue until punished for blue presses
        #press_yellow_earn_index: integer
            #How many times the buttone has been pressed 
            #while yellow until reinforced for yellow presses
        #press_blue_loss_index: integer
            #How many times the buttone has been pressed
            #while yellow until punishment for yellow presses
        #blue_interval_earn_value: tuple
            #A value compared against the probability of reinforcement
            #for blue RI schedule. Is between 0 and 1
        #blue_interval_loss_value: tuple
            #A value compared against the probability of punishment
            #for blue RI schedule. Is between 0 and 1
        #yellow_interval_earn_value: tuple
            #A value compared against the probability of reinforcement
            #for yellow RI schedule. Is between 0 and 1
        #yellow_interval_loss_value: tuple
            #A value compared against the probability of punishment
            #for yellow RI schedule. Is between 0 and 1
    
    #Return
    #------
    #point_earned: integer
        #A ternary value indicating whether a point was
        #gained, lost, or remained the same
    
    #Returns are otherwise the same as parameters, 
    #bar t and classes
    
    def handle_space_key(t, schedule_manager, flash_manager, points, button_response,
                         press_blue_earn_index, press_blue_loss_index,
                         press_yellow_earn_index, press_yellow_loss_index, sounds):
        
        #Handles reinforcement (earning) and punishment (loss) for both interval (time-based)
        #and ratio (press-based) schedules.
        
        #Parameters:
            #t: float
                #Current time in the routine.
            #schedule_manager: object
                #Manages schedule logic and intervals.
            #flash_manager: object
                #Handles flashing lights for reinforcement and punishment.
            #points: int
                #Current point total.
            #button_response: object
                #The response button (blue or yellow).
            #press_blue_earn_index, press_blue_loss_index: int
                #Current count of button presses for blue earning and loss schedules.
            #press_yellow_earn_index, press_yellow_loss_index: int
                #Current count of button presses for yellow earning and loss schedules.
                
        #Returns:
            #Updated variables for points, indices, and any state changes.
        
        point_earned = 0 #No point earned as a default
        
        ding = sounds['ding'] if sounds else None
        womp = sounds['womp'] if sounds else None
        
        if (button_response.fillColor == [-1, -1, 1]).all(): #If blue
            if (0 < schedule_manager.blue_i < float('inf')) or (0 < schedule_manager.blue_random_i < float('inf')): #Interval schedules
                if t >= schedule_manager.next_blue_earn_time:
                    points += int(schedule_manager.blue_mag)
                    point_earned = 1
                    schedule_manager.blue_fh_index += 1
                    schedule_manager.next_blue_earn_time = schedule_manager.calculate_next_blue_earn_time(button_response)
                    if schedule_manager.session_duration - t > 0.3:
                        flash_manager.start_flash('gl', t)
                        if ding is not None:
                            current_sound = play_sound(ding)
                        
            elif (0 < schedule_manager.blue_r < float('inf')) or (0 < schedule_manager.blue_random_r < float('inf')):#Ratio schedules
                press_blue_earn_index += 1
                if press_blue_earn_index >= round(schedule_manager.calculate_next_press_earn_requirement(button_response)):
                    points += int(schedule_manager.blue_mag)
                    point_earned = 1
                    press_blue_earn_index = 0
                    schedule_manager.blue_fh_index += 1
                    if schedule_manager.session_duration - t > 0.3:
                        flash_manager.start_flash('gl', t) 
                        if ding is not None:
                            current_sound = play_sound(ding)
            """ 
            This condition is current vestigial. I may re-add the probability per interval condition if there is demand. 
            
            elif schedule_manager.blue_random_r > 0:
                blue_ratio_earn_value = random_float()
                if schedule_manager.blue_random_r_chance >= blue_ratio_earn_value:
                    points += int(schedule_manager.blue_mag)
                    point_earned = 1
                    if schedule_manager.session_duration - t > 0.3:
                        flash_manager.start_flash('gl', t) # Start green light flash
                        current_sound = play_sound(ding)
                        
            elif schedule_manager.blue_random_i > 0 and schedule_manager.blue_random_i != float('inf'):
               if schedule_manager.blue_random_i_chance > schedule_manager.blue_interval_earn_value:
                    points += int(schedule_manager.blue_mag)
                    schedule_manager.blue_interval_earn_value = 1
                    point_earned = 1
                    if schedule_manager.session_duration - t > 0.3:
                        flash_manager.start_flash('gl', t) # Start green light flash
                        current_sound = play_sound(ding)
            """
            #Loss logic
            if (0 < schedule_manager.blue_pun_i < float('inf')) or (0 < schedule_manager.blue_pun_random_i < float('inf')):
                    points -= int(schedule_manager.blue_pun_mag)
                    point_earned = -1
                    schedule_manager.blue_pun_fh_index += 1
                    schedule_manager.next_blue_loss_time = schedule_manager.calculate_next_blue_loss_time(button_response)
                    if schedule_manager.session_duration - t > 0.3:
                        flash_manager.start_flash('rl', t)
                        if womp is not None:
                            current_sound = play_sound(womp) 
                        
            elif (0 < schedule_manager.blue_pun_r < float('inf')) or (0 < schedule_manager.blue_pun_random_r < float('inf')):
                press_blue_loss_index += 1
                if press_blue_loss_index >= round(schedule_manager.calculate_next_press_loss_requirement(button_response)):
                    points -= int(schedule_manager.blue_pun_mag)
                    point_earned = -1
                    press_blue_loss_index = 0
                    schedule_manager.blue_pun_fh_index += 1 
                    if schedule_manager.session_duration - t > 0.3:
                        flash_manager.start_flash('rl', t)
                        if womp is not None:
                            current_sound = play_sound(womp)
            """
            elif schedule_manager.blue_pun_random_r > 0 and schedule_manager.blue_pun_random_r != -float('inf'):
                blue_ratio_loss_value = random_float()
                if schedule_manager.blue_pun_random_r_chance >= blue_ratio_loss_value:
                    points -= int(schedule_manager.blue_pun_mag)
                    point_earned = -1
                    if schedule_manager.session_duration - t > 0.3:
                        flash_manager.start_flash('rl', t)
                        current_sound = play_sound(womp
                                                   
            #elif schedule_manager.blue_pun_random_i > 0 and schedule_manager.blue_pun_random_i != -float('inf'):
                #if schedule_manager.blue_pun_random_i_chance > schedule_manager.blue_interval_loss_value:
                    #points -= int(schedule_manager.blue_pun_mag)
                    #schedule_manager.blue_interval_loss_value = 1
                    #point_earned = -1
                    #if schedule_manager.session_duration - t > 0.3:
                        #flash_manager.start_flash('rl', t)
                        #current_sound = play_sound(womp)
            """
        # Handle Yellow Button
        elif (button_response.fillColor == [1, 1, -1]).all(): #If yellow
            # Earning Logic
            if (0 < schedule_manager.yellow_i < float('inf')) or (0 < schedule_manager.yellow_random_i < float('inf')):
                if t >= schedule_manager.next_yellow_earn_time:
                    points += int(schedule_manager.yellow_mag)
                    point_earned = 1
                    schedule_manager.yellow_fh_index += 1
                    schedule_manager.next_yellow_earn_time = schedule_manager.calculate_next_yellow_earn_time(button_response)
                    if schedule_manager.session_duration - t > 0.3:
                        flash_manager.start_flash('gl', t) 
                        if ding is not None:
                            current_sound = play_sound(ding)
                        
            elif (0 < schedule_manager.yellow_r < float('inf')) or (0 < schedule_manager.yellow_random_r < float('inf')):
                press_yellow_earn_index += 1
                if press_yellow_earn_index >= round(schedule_manager.calculate_next_press_earn_requirement(button_response)):
                    points += int(schedule_manager.yellow_mag)
                    point_earned = 1
                    press_yellow_earn_index = 0
                    schedule_manager.yellow_fh_index += 1
                    if schedule_manager.session_duration - t > 0.3:
                        flash_manager.start_flash('gl', t)
                        if ding is not None:
                            current_sound = play_sound(ding)
                        
            """
            elif schedule_manager.yellow_random_r > 0 and schedule_manager.yellow_random_r != -float('inf'):
                yellow_ratio_earn_value = random_float()
                if schedule_manager.yellow_random_r_chance >= yellow_ratio_earn_value:
                    points += int(schedule_manager.blue_mag)
                    point_earned = 1
                    if schedule_manager.session_duration - t > 0.3:
                        flash_manager.start_flash('gl', t)
                        current_sound = play_sound(ding)
                        
            elif schedule_manager.yellow_random_i > 0 and schedule_manager.yellow_random_i != -float('inf'):
                if schedule_manager.yellow_random_i_chance > schedule_manager.yellow_interval_earn_value:
                    points += int(schedule_manager.yellow_mag)
                    schedule_manager.yellow_interval_earn_value = 1
                    point_earned = 1
                    if schedule_manager.session_duration - t > 0.3:
                        flash_manager.start_flash('gl', t)
                        current_sound = play_sound(ding)
            """
            #Loss Logic
            if (0 < schedule_manager.yellow_pun_i < float('inf')) or (0 < schedule_manager.yellow_pun_random_i < float('inf')):
                if t >= schedule_manager.calculate_next_yellow_loss_time(button_response):
                    points -= int(schedule_manager.yellow_pun_mag)
                    point_earned = -1
                    schedule_manager.yellow_pun_fh_index += 1
                    schedule_manager.next_yellow_loss_time = schedule_manager.calculate_next_yellow_loss_time(button_response)
                    if schedule_manager.session_duration - t > 0.3:
                        flash_manager.start_flash('rl', t)
                        if womp is not None:
                            current_sound = play_sound(womp)
                        
            elif (0 < schedule_manager.yellow_pun_r < float('inf')) or (0 < schedule_manager.yellow_pun_random_r < float('inf')): # Ratio schedule (press-based)
                press_yellow_loss_index += 1
                if press_yellow_loss_index >= round(schedule_manager.calculate_next_press_loss_requirement(button_response)):
                    points -= int(schedule_manager.yellow_pun_mag)
                    point_earned = -1
                    press_yellow_loss_index = 0
                    schedule_manager.yellow_pun_fh_index += 1
                    if schedule_manager.session_duration - t > 0.3:
                        flash_manager.start_flash('rl', t)
                        if womp is not None:
                            current_sound = play_sound(womp)
                        
            """
            elif schedule_manager.yellow_pun_random_r > 0 and schedule_manager.yellow_pun_random_r != -float('inf'):
                yellow_ratio_loss_value = random_float()
                if schedule_manager.yellow_pun_random_r_chance >= yellow_ratio_loss_value:
                    points -= int(schedule_manager.yellow_pun_mag)
                    point_earned = -1
                    if schedule_manager.session_duration - t > 0.3:
                        flash_manager.start_flash('rl', t)
                        current_sound = play_sound(womp)
                        
            elif schedule_manager.yellow_pun_random_i > 0 and schedule_manager.yellow_pun_random_i != -float('inf'):
                if schedule_manager.yellow_pun_random_i_chance > schedule_manager.yellow_interval_loss_value:
                    points -= int(schedule_manager.yellow_pun_mag)
                    schedule_manager.yellow_interval_loss_value = 1
                    point_earned = -1
                    if schedule_manager.session_duration - t > 0.3:
                        flash_manager.start_flash('rl', t)
                        current_sound = play_sound(womp)
            """
        # Return updated variables
        return (points, point_earned,
                press_blue_earn_index, press_blue_loss_index,
                press_yellow_earn_index, press_yellow_loss_index)
                
    def collect_space():
        thisExp.addData('SessionNumber', f"#{session_number}")
        thisExp.addData('Time', t) #Time is session
        thisExp.addData('Points', points) #Number of points
        thisExp.addData('Point Earned', point_earned) #Ternary value
        thisExp.addData('During Changeover?', in_changeover_delay) #Press occurred outside of changeover delay 
        thisExp.addData('CurrentSchedule', current_schedule) #Current schedule
        thisExp.addData('Button', 'Blue' if check_colors(button_response.fillColor, button_color1) else 'Yellow') #button color
        thisExp.nextEntry() #adds entry
    
    #Handles presses related to the tab key.
    
    #Parameters
    #__________
    #t: float
        #Current time in experiment, same as handle_space_key()
    
    #flash_manager: class
        #Imports logic for flashes
        
    #button_response: object
        #The response button, for color changes
        
    #schedule_manager: class
        #Needed for changeover delay
    
    def handle_tab_key(t, flash_manager,
                button_response, schedule_manager):
                    
        flash_manager.start_flash('cycle', t) #Handles flash of the cycle button
    
        #Switches button color
        if check_colors(button_response.fillColor, button_color1):
            button_response.fillColor = button_color2
        else:
            button_response.fillColor = button_color1
    
        schedule_manager.last_switch_time = t #value for changeover delay
        return False
    
    #Collects tab data
    def collect_tab():
        thisExp.addData('SessionNumber', f"#{session_number}")
        thisExp.addData('Time', t) #Session time
        thisExp.addData('Points', points) #Number of points
        thisExp.addData('Point Earned', 'N/A') #No ternary value as the changeover key does not affect current points
        thisExp.addData('During Changeover?', in_changeover_delay) 
        thisExp.addData('CurrentSchedule', current_schedule) #Current schedule
        thisExp.addData('Button', 'Tab') #Records button as tab
        thisExp.nextEntry() #Adds entry
        
    #Draws the experiment, includes logic for schedule lights
    
    #Paramaters:
        #win: object
            #The PsychoPy window
        #green_light: object
            #Reinforcement light
        #red_light: object
            #Punishment light
        #button_response: object
            #The response button
        #button_cycle: object
            #The switch button
        #switch_text: object
            #button_cycle label
        #points_display: object
            #Shows how many points the subject has earned
        #lights: list of objects
            #Schedule lights, condensed for my own sanity
        #current_schedule: string, but converted to integer
            #The current schedule, determines which schedule light is on.
    
    def draw_main(win, schedule_manager, 
                  context_image,
                  green_light, red_light,
                  button_response, button_cycle,
                  switch_text, points_display,
                  lights, current_schedule):
        
        win.clearBuffer()
    
        if schedule_manager.schedule_lights.upper() == 'ON':
            total_lights = len(all_schedules)
    
            spacing = 0.15
    
            # --- Compute starting position (AutoJS-compatible) ---
            if total_lights % 2 == 0:
                start_position = -(total_lights / 2 - 0.5) * spacing
            else:
                start_position = -int(total_lights / 2) * spacing
    
            # --- Build positions list (AutoJS translates cleanly) ---
            positions = []
            for i in range(total_lights):
                positions.append(start_position + i * spacing)
    
            # --- LOOP THROUGH LIGHTS (NO DICTIONARIES) ---
            # lights = [light_1, light_2, ..., light_n]
            for i in range(total_lights):
                light = lights[i]
    
                # Set position (JS-safe)
                light.pos = [positions[i], 0.4]
    
                # Turn the current light "on" or "off"
                if (i + 1) == int(current_schedule):
                    light.setFillColor(light_on, 'rgb')
                else:
                    light.setFillColor(light_off, 'rgb')
    
                # Draw
                light.draw()
        
        # Draws everything else
        if schedule_manager.context_path is not None:
            context_image.draw()
        green_light.draw()
        red_light.draw()
        button_response.draw()
        button_cycle.draw()
        switch_text.draw()
        points_display.draw()
        win.flip()
        
    #Draws objects for the blackout period.
    
    #Parameters
    #----------
    #win: obj
        #Psychopy window
    #green_light_bo: object
        #Blacked out green_light
    #red_light_bo: object
        #Blacked out red_light
    #timer_text: object
        #Text for the timer, includes countdown
    #points_display: object
        #Shows how many points have been earned
    #response_bo: object
        #Blacked out response button
    #button_cycle_bo:
        #Blacked out switch button
    
    def draw_break(win, green_light_bo, red_light_bo,
                    timer_text, points_display,
                    response_bo, button_cycle_bo):
        #Draws everything
        green_light_bo.draw()
        red_light_bo.draw()
        points_display.draw()
        response_bo.draw()
        button_cycle_bo.draw()
        timer_text.draw()
        win.flip() #updates screen
        
    
    #Makes sure schedule data can include None values.
    #This is essential as you don't want multiple schedules
    #active on the same color.
    
    #Parameter
    #---------
    #value: string
        #Values are from the DataFrame
    
    #Return
    #------
    #None: None
        #Allows for values to be none
    
    def safe_float(value):
        try:
            if isinstance(value, pd.Series):
                value = value.iloc[0]
            if pd.isna(value):
                return None
            return float(value)
        except (TypeError, ValueError):
            return None
            
    def safe_string(value):
        
        #Cleans and extracts the relevant string value from mixed input formats.
    
        #Parameters:
        #value (str): The input value to be cleaned and processed.
    
        #Returns:
        #str: The cleaned string in uppercase, or None if invalid.
        
        try:
            if isinstance(value, pd.Series):
                value = value.iloc[0]  # Handle series objects
            if pd.isna(value) or not isinstance(value, str):
                return None  # Return None for invalid or empty values
            return str(value).strip().split()[-1].upper()  # Extract last word and clean
        except Exception:
            return None
            
    def safe_tuple(value):
        if pd.isna(value) or value in ['', None]:
            return default
        if isinstance(value, str):
                return tuple(eval(value))
        return value
    
    def safe_bool(value):
        # Handle Series
        if isinstance(value, pd.Series):
            if len(value) == 0:
                return False
            value = value.iloc[0]
    
        # Handle NaN / None
        if value is None or pd.isna(value):
            return False
    
        # Normalize
        value = str(value).strip().lower()
    
        return value not in ['x', '', '0', 'false', 'none']
    
    #Function to handle blackout periods.
    
    #Parameters
    #----------
    #win: object
        #PsychoPy window
    #blackout_timer: object
        #Gives a countdown for the blackout period
    #points_display: object
        #Shows total points earned
    #response_bo: object
        #Blacked out response button
    #button_cycle_bo: object
        #Blacked out switch button
    #green_light_bo: object
        #Blacked out green_light
    #red_light_bo: object
        #Blacked out red_light
    
    def handle_blackout_period(win, blackout_timer, 
                            points_display, response_bo, 
                            button_cycle_bo, green_light_bo,
                            red_light_bo):
        #Initializes blackout period
        blackout_period = True 
        blackout_start_time = core.getTime()
        blackout_timer.reset() #resets blackout timer
    
        while blackout_period:
            current_time = core.getTime()
            elapsed_time = current_time - blackout_start_time
            remaining_time = max(0, int(blackout_timer.getTime())) #Value for timer
            end_keys = event.getKeys(['escape'])
            if 'escape' in end_keys:
                sys.exit()
            if remaining_time > 0:
                #Countdown
                timer_text = visual.TextStim(win, 
                                    text=f"Time Remaining: {remaining_time}",
                                    pos=(0, 0), height=0.05, color='black')
                                    
                draw_break(win, green_light_bo, red_light_bo,
                            timer_text, points_display, response_bo, 
                            button_cycle_bo)
            else:
                #Prompts the user to hit 'enter' to advance to the next session
                timer_text = visual.TextStim(win,
                            text="Hit 'enter' to continue",
                            pos=(0, 0), height=0.05,
                            color='black')
                
                #Draws required objects
                draw_break(win, green_light_bo, red_light_bo,
                            timer_text, points_display,
                            response_bo, button_cycle_bo)
    
                #Makes 'enter' a valid input, remember return = enter
                keys = event.getKeys(['return'])
    
                if 'return' in keys: #if enter is pressed 
                    blackout_period = False  #blackout period ends
        win.flip() #Updates screen
    
    def preload_contexts(schedule_df, win):
        context_cache = {}
    
        for row in schedule_df.to_dict('records'):
            schedule_id = row.get('Schedule_number')  # adjust if different column name
            path = row.get('Context_Path')
    
            # Skip schedules without a valid context
            if pd.isna(path) or str(path).strip() == '':
                context_cache[schedule_id] = None
                continue
    
            try:
                pos = safe_tuple(row.get('Context_Position'))
                size = safe_tuple(row.get('Context_Size'))
                opacity = row.get('Context_Opacity')
                depth = row.get('Context_Depth')
    
                if pd.isna(opacity):
                    opacity = 1
                if pd.isna(depth):
                    depth = 0
    
                context_image = visual.ImageStim(
                    win=win,
                    name=f'context_{schedule_id}',
                    image=str(path).strip(),
                    pos=pos,
                    size=size,
                    opacity=float(opacity),
                    depth=float(depth)
                )
    
                context_cache[schedule_id] = context_image
    
            except Exception as e:
                print(f"Error preloading schedule {schedule_id}: {e}")
                context_cache[schedule_id] = None
    
        return context_cache
    
    def get_context(context_cache, current_schedule):
        return context_cache.get(current_schedule, None)
    
    def preload_sounds(schedule_df):
        sound_cache = {}
        for row in schedule_df.to_dict('records'):
            schedule_id = row.get('Schedule_number')
            ding_path = row.get('Ding_Path')
            womp_path = row.get('Womp_Path')
    
            # Skip schedules without valid sound paths
            if (pd.isna(ding_path) or str(ding_path).strip() == '') and \
               (pd.isna(womp_path) or str(womp_path).strip() == ''):
                sound_cache[schedule_id] = None
                continue
    
            try:
                ding = sound.Sound(str(ding_path).strip()) if not pd.isna(ding_path) else None
                womp = sound.Sound(str(womp_path).strip()) if not pd.isna(womp_path) else None
                sound_cache[schedule_id] = {'ding': ding, 'womp': womp}
            except Exception as e:
                print(f"Error preloading schedule {schedule_id}: {e}")
                sound_cache[schedule_id] = None
    
        return sound_cache
    
    def get_sounds(sound_cache, current_schedule):
        return sound_cache.get(current_schedule, None)
        
    #Initialization to band-aid a problem   
    button_response.fillColor == button_color1
    
    context_cache = preload_contexts(schedule_df, win)
    sound_cache = preload_sounds(schedule_df)
    
    # --- Initialize components for Routine "Goodbye" ---
    # Run 'Begin Experiment' code from goodbye
    from psychopy import visual, core, event, data
    
    #Goodbye Message
    goodbye_message = visual.TextStim(win,
        text="Thank you for completing the experiment. Your responses are recorded and you are free to leave the window. Please hit the 'Esc' button to exit the experiment",
        height=0.05, color=[1,1,1], pos=[0, 0])
    
    def draw_goodbye():
        goodbye_message.draw()
        win.flip()
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Welcome" ---
    # create an object to store info about Routine Welcome
    Welcome = data.Routine(
        name='Welcome',
        components=[],
    )
    Welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from welcome_and_data_collection
    #Initializes routine boolean
    welcome = True
    # store start times for Welcome
    Welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Welcome.tStart = globalClock.getTime(format='float')
    Welcome.status = STARTED
    Welcome.maxDuration = None
    # keep track of which components have finished
    WelcomeComponents = Welcome.components
    for thisComponent in Welcome.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Welcome" ---
    Welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from welcome_and_data_collection
        while welcome:
            end_keys = event.getKeys(['escape'])
            if 'escape' in end_keys:
                sys.exit()
            keys = event.getKeys(['return']) #If enter is pressed
            draw_welcome()
            if 'return' in keys: 
                welcome = False #Ends routine
                win.flip()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Welcome,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Welcome.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Welcome" ---
    for thisComponent in Welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Welcome
    Welcome.tStop = globalClock.getTime(format='float')
    Welcome.tStopRefresh = tThisFlipGlobal
    thisExp.nextEntry()
    # the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Selection_type = data.TrialHandler2(
        name='Selection_type',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(Selection_type)  # add the loop to the experiment
    thisSelection_type = Selection_type.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSelection_type.rgb)
    if thisSelection_type != None:
        for paramName in thisSelection_type:
            globals()[paramName] = thisSelection_type[paramName]
    
    for thisSelection_type in Selection_type:
        Selection_type.status = STARTED
        if hasattr(thisSelection_type, 'status'):
            thisSelection_type.status = STARTED
        currentLoop = Selection_type
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisSelection_type.rgb)
        if thisSelection_type != None:
            for paramName in thisSelection_type:
                globals()[paramName] = thisSelection_type[paramName]
        
        # --- Prepare to start Routine "Trial" ---
        # create an object to store info about Routine Trial
        Trial = data.Routine(
            name='Trial',
            components=[],
        )
        Trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from omnicode
        flash_manager = FlashManager() #'imports' FlashManager() as 'flash_manager'
        routine_clock = core.Clock()
        routine_clock.reset() #Resets routine_clock
        
        #Initializes booleans
        routine_active = True
        switch_enabled = True
        tab_pressed = False
        continue_routine = True
        current_sound = None
        transition_to_extinction = False
        extinction = False
        
        #Resets indicies to 0
        press_blue_earn_index = 0
        press_blue_loss_index = 0
        press_yellow_earn_index = 0
        press_yellow_loss_index = 0
        
        #Reset proc values
        blue_earn_proc_value = 1
        blue_loss_proc_value = 1
        yellow_earn_proc_value = 1
        yellow_loss_proc_value = 1
        
        session_number += 1
        
        #Initializes available_schedules
        available_schedules = list(set(all_schedules) - set(used_schedules))
        
        #Tests is data from CSV is properly extracted
        try:
            current_schedule = get_new_schedule()
            #'Imports' DataFrame
            schedule_data = schedule_df.loc[
            schedule_df['Schedule_number'] == current_schedule].iloc[0]
            schedule_manager = ScheduleManager(
                safe_float(schedule_data['Blue_Interval']), safe_float(schedule_data['Yellow_Interval']),
                safe_float(schedule_data['Blue_Pun_Interval']), safe_float(schedule_data['Yellow_Pun_Interval']),
                safe_float(schedule_data['Blue_Ratio']), safe_float(schedule_data['Yellow_Ratio']),
                safe_float(schedule_data['Blue_Pun_Ratio']), safe_float(schedule_data['Yellow_Pun_Ratio']),
                safe_float(schedule_data['Blue_Random_Ratio']), safe_float(schedule_data['Yellow_Random_Ratio']),
                safe_float(schedule_data['Blue_Pun_Random_Ratio']), safe_float(schedule_data['Yellow_Pun_Random_Ratio']),
                safe_float(schedule_data['Blue_Random_Interval']), safe_float(schedule_data['Yellow_Random_Interval']),
                safe_float(schedule_data['Blue_Pun_Random_Interval']), safe_float(schedule_data['Yellow_Pun_Random_Interval']),
                safe_bool(schedule_data['Blue_FH']), safe_bool(schedule_data['Yellow_FH']),
                safe_bool(schedule_data['Blue_Pun_FH']), safe_bool(schedule_data['Yellow_Pun_FH']),
                safe_float(schedule_data['Blue_FH_Intervals']), safe_float(schedule_data['Yellow_FH_Intervals']),
                safe_float(schedule_data['Blue_Pun_FH_Intervals']), safe_float(schedule_data['Yellow_Pun_FH_Intervals']),
                safe_string(schedule_data['Blue_FH_Type']), safe_string(schedule_data['Yellow_FH_Type']),
                safe_string(schedule_data['Blue_Pun_FH_Type']), safe_string(schedule_data['Yellow_Pun_FH_Type']),
                safe_float(schedule_data['Session_Duration']), safe_float(schedule_data['Blue_Mag']),
                safe_float(schedule_data['Yellow_Mag']), safe_float(schedule_data['Blue_Pun_Mag']),
                safe_float(schedule_data['Yellow_Pun_Mag']), safe_float(schedule_data['Changeover_Delay']),
                safe_float(schedule_data['Blackout_Duration']),
                safe_string(schedule_data['Blue_Distribution']), safe_string(schedule_data['Yellow_Distribution']),
                safe_string(schedule_data['Blue_Pun_Distribution']), safe_string(schedule_data['Yellow_Pun_Distribution']),
                safe_float(schedule_data['SD_Blue']), safe_float(schedule_data['SD_Yellow']),
                safe_float(schedule_data['SD_Blue_Pun']), safe_float(schedule_data['SD_Yellow_Pun']),
                safe_string(schedule_data['Schedule_Lights']), safe_string(schedule_data['Context_Path']),
                safe_tuple(schedule_data['Context_Position']), safe_tuple(schedule_data['Context_Size']),
                safe_float(schedule_data['Context_Opacity']), safe_float(schedule_data['Context_Depth']),
                safe_string(schedule_data['Ding_Path']), safe_string(schedule_data['Womp_Path'])
               )
            
            #If everything works properly, the program will proceed to the main loop
            schedule_loaded = True
            context_image = get_context(context_cache, current_schedule)
            sounds = get_sounds(sound_cache, current_schedule)
            schedule_manager.reset_times()
            blackout_timer = core.CountdownTimer(schedule_manager.blackout_duration + 1)
            print(f"first schedule: {current_schedule}")
            schedule_manager.calculate_next_yellow_earn_time(button_response)
            schedule_manager.generate_fleshler_hoffman_list()
            print(f"Blue_FH: {schedule_manager.blue_fh_list}")
            print(f"Yellow_FH: {schedule_manager.yellow_fh_list}")
            routine_active = True
            continue_routine = True
            win.flip()
         
        except Exception as e:
            if current_schedule not in schedule_df['Schedule_number'].values:
                print(f"Schedule {current_schedule} not found in DataFrame")
            print(f"Error loading schedule: {e}")
            continue_routine = False
        
        # store start times for Trial
        Trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Trial.tStart = globalClock.getTime(format='float')
        Trial.status = STARTED
        thisExp.addData('Trial.started', Trial.tStart)
        Trial.maxDuration = None
        # keep track of which components have finished
        TrialComponents = Trial.components
        for thisComponent in Trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Trial" ---
        Trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisSelection_type, 'status') and thisSelection_type.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from omnicode
            while continue_routine:
                end_keys = event.getKeys(['escape'])
                if 'escape' in end_keys:
                        sys.exit()
            
                if routine_active:
                    t = routine_clock.getTime()# Get current time
                    #Defines changeover delay
                    in_changeover_delay = (t - schedule_manager.last_switch_time < schedule_manager.changeover_delay)
                    keys = event.getKeys(['space', 'tab'])
                    #schedule_manager.generate_one_second_interval() #Interval generator for RI schedules
                    
                    # Process tab press outside changeover delay
                    if in_changeover_delay and 'tab' in keys:
                        keys.remove('tab')
                        collect_tab()
                    tab_pressed = 'tab' in keys
            
                    # Handle space key logic
                    if 'space' in keys and in_changeover_delay == False:
                        points, point_earned, press_blue_earn_index, \
                        press_blue_loss_index, press_yellow_earn_index, \
                        press_yellow_loss_index=\
                        handle_space_key(t, schedule_manager, flash_manager, points,
                                button_response, press_blue_earn_index,
                                press_blue_loss_index, press_yellow_earn_index,
                                press_yellow_loss_index, sounds)
                        points_display.text = f'Points: {points}'
                        flash_manager.start_flash('rb', t)
                        collect_space()
                    elif 'space' in keys and in_changeover_delay == True: 
                        #Still play animation, data collection notes
                        #that the press occurred during the changeover delay
                        flash_manager.start_flash('rb', t)
                        collect_space()
                        
                    # Handle tab press to change button color
                    if tab_pressed == True and in_changeover_delay == False:
                        switch_enabled = handle_tab_key(t, flash_manager, button_response, schedule_manager)
                        collect_tab()
            
                    # Update flashes and redraw interface
                    flash_manager.update_flashes(t, green_light, red_light, button_response, button_cycle)
                    draw_main(win, schedule_manager, context_image, green_light, red_light,
                              button_response, button_cycle, switch_text, points_display, lights, current_schedule)
            
                    # End session if session duration is reached
                    if t >= schedule_manager.session_duration:
                        routine_active = False
                        blackout_timer.reset()
            
                # Manage blackout period logic
                else:
                    handle_blackout_period(win, blackout_timer, points_display, response_bo, button_cycle_bo, green_light_bo, red_light_bo)
                    # Attempt to switch to a new schedule
                    if len(all_schedules) > len(used_schedules):
                        current_schedule = get_new_schedule()
                        schedule_data = schedule_df.loc[schedule_df['Schedule_number'] == current_schedule].iloc[0]
                        schedule_manager = ScheduleManager(
                            safe_float(schedule_data['Blue_Interval']), safe_float(schedule_data['Yellow_Interval']),
                            safe_float(schedule_data['Blue_Pun_Interval']), safe_float(schedule_data['Yellow_Pun_Interval']),
                            safe_float(schedule_data['Blue_Ratio']), safe_float(schedule_data['Yellow_Ratio']),
                            safe_float(schedule_data['Blue_Pun_Ratio']), safe_float(schedule_data['Yellow_Pun_Ratio']),
                            safe_float(schedule_data['Blue_Random_Ratio']), safe_float(schedule_data['Yellow_Random_Ratio']),
                            safe_float(schedule_data['Blue_Pun_Random_Ratio']), safe_float(schedule_data['Yellow_Pun_Random_Ratio']),
                            safe_float(schedule_data['Blue_Random_Interval']), safe_float(schedule_data['Yellow_Random_Interval']),
                            safe_float(schedule_data['Blue_Pun_Random_Interval']), safe_float(schedule_data['Yellow_Pun_Random_Interval']),
                            safe_bool(schedule_data['Blue_FH']), safe_bool(schedule_data['Yellow_FH']),
                            safe_bool(schedule_data['Blue_Pun_FH']), safe_bool(schedule_data['Yellow_Pun_FH']),
                            safe_float(schedule_data['Blue_FH_Intervals']), safe_float(schedule_data['Yellow_FH_Intervals']),
                            safe_float(schedule_data['Blue_Pun_FH_Intervals']), safe_float(schedule_data['Yellow_Pun_FH_Intervals']),
                            safe_string(schedule_data['Blue_FH_Type']), safe_string(schedule_data['Yellow_FH_Type']),
                            safe_string(schedule_data['Blue_Pun_FH_Type']), safe_string(schedule_data['Yellow_Pun_FH_Type']),
                            safe_float(schedule_data['Session_Duration']), safe_float(schedule_data['Blue_Mag']),
                            safe_float(schedule_data['Yellow_Mag']), safe_float(schedule_data['Blue_Pun_Mag']),
                            safe_float(schedule_data['Yellow_Pun_Mag']), safe_float(schedule_data['Changeover_Delay']),
                            safe_float(schedule_data['Blackout_Duration']),
                            safe_string(schedule_data['Blue_Distribution']), safe_string(schedule_data['Yellow_Distribution']),
                            safe_string(schedule_data['Blue_Pun_Distribution']), safe_string(schedule_data['Yellow_Pun_Distribution']),
                            safe_float(schedule_data['SD_Blue']), safe_float(schedule_data['SD_Yellow']),
                            safe_float(schedule_data['SD_Blue_Pun']), safe_float(schedule_data['SD_Yellow_Pun']),
                            safe_string(schedule_data['Schedule_Lights']),
                            safe_string(schedule_data['Context_Path']), safe_tuple(schedule_data['Context_Position']),
                            safe_tuple(schedule_data['Context_Size']), safe_float(schedule_data['Context_Opacity']),
                            safe_float(schedule_data['Context_Depth']),
                            safe_string(schedule_data['Ding_Path']), safe_string(schedule_data['Womp_Path'])
                           )
                        routine_clock.reset()
                        press_blue_earn_index = press_blue_loss_index = press_yellow_earn_index = press_yellow_loss_index = 0
                        blue_earn_proc_value = blue_loss_proc_value = yellow_earn_proc_value = yellow_loss_proc_value = 1
                        blue_fh_index = yellow_fh_index = blue_pun_fh_index = yellow_pun_fh_index = 0
                        schedule_manager.interval_start = 0
                        context_image = get_context(context_cache, current_schedule)
                        event.clearEvents()
                        session_number += 1
                        print(current_schedule)
                        print(f"Blue_FH: {schedule_manager.blue_fh_list}")
                        print(f"Yellow_FH: {schedule_manager.yellow_fh_list}")
                        event.clearEvents()
                        routine_active = True
                    else:
                        break
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=Trial,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Trial.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Trial" ---
        for thisComponent in Trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Trial
        Trial.tStop = globalClock.getTime(format='float')
        Trial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Trial.stopped', Trial.tStop)
        # Run 'End Routine' code from omnicode
        #For repeated runs:
        
        #Restablishes Schedules
        all_schedules = list(schedule_df['Schedule_number'])
        
        #Removes 'EXT', 'ACQ', and Tutorial from trial block
        try:
            all_schedules.remove('EXT')
            all_schedules.remove('ACQ')
            all_schedules.remove('Tutorial')
            all_schedules.remove('Keyboard_Tutorial')
        #Program will still run if any or all are missing
        except ValueError:
            pass
        #Prints schedules for debugging. I strongly suggest keeping this.
        print(all_schedules)
        print(f"number of initial schedules: {len(all_schedules)}")
        
        #Sets used schedules to empty
        used_schedules = []
        
        event.clearEvents()
        # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisSelection_type as finished
        if hasattr(thisSelection_type, 'status'):
            thisSelection_type.status = FINISHED
        # if awaiting a pause, pause now
        if Selection_type.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            Selection_type.status = STARTED
    # completed 1.0 repeats of 'Selection_type'
    Selection_type.status = FINISHED
    
    
    # --- Prepare to start Routine "Goodbye" ---
    # create an object to store info about Routine Goodbye
    Goodbye = data.Routine(
        name='Goodbye',
        components=[],
    )
    Goodbye.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from goodbye
    #Initializes Goodbye
    goodbye = True
    draw_goodbye()
    # store start times for Goodbye
    Goodbye.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Goodbye.tStart = globalClock.getTime(format='float')
    Goodbye.status = STARTED
    thisExp.addData('Goodbye.started', Goodbye.tStart)
    Goodbye.maxDuration = None
    # keep track of which components have finished
    GoodbyeComponents = Goodbye.components
    for thisComponent in Goodbye.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Goodbye" ---
    Goodbye.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from goodbye
        while goodbye:
            keys = event.getKeys(['return'])
            draw_goodbye()
            if 'return' in keys: #Ends experiment
                goodbye = False
                win.flip()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Goodbye,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Goodbye.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Goodbye.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Goodbye" ---
    for thisComponent in Goodbye.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Goodbye
    Goodbye.tStop = globalClock.getTime(format='float')
    Goodbye.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Goodbye.stopped', Goodbye.tStop)
    thisExp.nextEntry()
    # the Routine "Goodbye" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
