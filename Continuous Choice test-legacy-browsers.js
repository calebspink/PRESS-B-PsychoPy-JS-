/******************************* 
 * Continuous Choice Test *
 *******************************/


// store info about the experiment session:
let expName = 'Continuous Choice test';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// Initializations to appease the gods, these do nothing else
let currentLoop;
let frameDur;
let WelcomeClock = [];
let routine_clock = [];
let TrialClock = [];
let GoodbyeClock = [];
let globalClock = [];
let routineTimer = [];
let t = 0;
let frameN = 0;
let continueRoutine = true;
let routineForceEnded = false;
let WelcomeMaxDurationReached = false;

// --- Added: per-routine MaxDurationReached flags (same pattern as WelcomeMaxDurationReached) ---
let TrialMaxDurationReached = false;
let GoodbyeMaxDurationReached = false;

// --- Added: MaxDuration values assigned as null inside each RoutineBegin ---
let WelcomeMaxDuration = null;
let TrialMaxDuration = null;
let GoodbyeMaxDuration = null;

// --- Added: component arrays iterated in RoutineEnd functions ---
let WelcomeComponents = [];
let TrialComponents = [];
let GoodbyeComponents = [];

// --- Added: loop handler referenced in LoopEnd and TrialRoutineBegin ---
let Selection_type;

// --- Added: welcome flag set inside WelcomeRoutineBegin ---
let welcome = false;
async function debugPaths() {
    const testPaths = [
        'PRESS-B_Schedule_Entry.csv',
        'resources/PRESS-B_Schedule_Entry.csv',
        'stimuli/PRESS-B_Schedule_Entry.csv',
        'stimuli/contexts/PRESS-B_Schedule_Entry.csv',
        'data/PRESS-B_Schedule_Entry.csv',
        '../PRESS-B_Schedule_Entry.csv',
    ];

    for (const path of testPaths) {
        try {
            const res = await fetch(path);
            console.log(`✅ FOUND at: ${path} (status ${res.status})`);
        } catch (e) {
            console.log(`❌ NOT found at: ${path}`);
        }
    }
}
debugPaths();
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'fill',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(WelcomeRoutineBegin());
flowScheduler.add(WelcomeRoutineEachFrame());
flowScheduler.add(WelcomeRoutineEnd());
const Selection_typeLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Selection_typeLoopBegin(Selection_typeLoopScheduler));
flowScheduler.add(Selection_typeLoopScheduler);
flowScheduler.add(Selection_typeLoopEnd);


flowScheduler.add(GoodbyeRoutineBegin());
flowScheduler.add(GoodbyeRoutineEachFrame());
flowScheduler.add(GoodbyeRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your participation!', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your participation!', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'PRESS-B_Schedule_Entry.csv', 'path': 'PRESS-B_Schedule_Entry.csv'},
    {'name': 'stimuli/contexts/desert_context.jpg', 'path': 'stimuli/contexts/desert_context.jpg'},
    {'name': 'stimuli/contexts/grassland_context.jpg', 'path': 'stimuli/contexts/grassland_context.jpg'},
    {'name': 'stimuli/contexts/snow_context.jpg', 'path': 'stimuli/contexts/snow_context.jpg'},
    {'name': 'stimuli/contexts/swamp_context.jpg', 'path': 'stimuli/contexts/swamp_context.jpg'},
    {'name': 'stimuli/ha.wav', 'path': 'stimuli/ha.wav'},
    {'name': 'stimuli/ding.wav', 'path': 'stimuli/ding.wav'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.WARNING);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2025.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + ("./" + `${expInfo["participant"]}_${expName}_${expInfo["date"]}`));
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "Welcome"
  WelcomeClock = new util.Clock();
  // Run 'Begin Experiment' code from welcome_and_data_collection
  let schedule_df = [];
  let all_schedules = [];
  
  let csvRaw = psychoJS.serverManager.getResource('PRESS-B_Schedule_Entry.csv');
  if (!csvRaw) {
      throw new Error("CSV failed to load from PsychoJS resources.");
  }
  
  let csvText;
  if (typeof csvRaw === 'string') {
      csvText = csvRaw;
  } else {
      csvText = new TextDecoder('utf-8').decode(csvRaw);
  }
  
  const lines = csvText
      .replace(/\r\n/g, '\n')
      .replace(/\r/g, '\n')
      .trim()
      .split('\n')
      .filter(line => line.trim() !== '');
  
  const headers = lines[0].split(',').map(h => h.trim());
  
  window.schedule_df = lines.slice(1).map(line => {
      const values = line.split(',');
      let obj = {};
      headers.forEach((h, i) => {
          let val = values[i] !== undefined ? values[i].trim() : '';
          obj[h] = (val === 'x' || val === '') ? null :
                   (!isNaN(val) && val !== '' ? Number(val) : val);
      });
      return obj;
  });
  
  window.schedule_df = window.schedule_df.filter(row =>
      row.Schedule_number !== null &&
      row.Schedule_number !== undefined &&
      String(row.Schedule_number).trim() !== ''
  );
  
  window.all_schedules = window.schedule_df
      .map(row => String(row.Schedule_number).trim())
      .filter(s => !['EXT', 'ACQ', 'Tutorial', 'Keyboard_Tutorial'].includes(s));
  
  console.log("CSV parsed successfully. Schedules found:", window.all_schedules);
  
  // Welcome message
  window.welcome_message = new visual.TextStim({
      win: psychoJS.window,
      name: 'welcome_message',
      text: "Hello, thank you for participating in the experiment.\n" +
            "If you wish to stop participating, hit the 'Escape' key; however, you will not receive sona credit.\n" +
            "Hit 'Enter' when you are ready to begin.",
      height: 0.05,
      color: new util.Color([1, 1, 1]),
      pos: [0, 0],
      units: 'height'
  });
  // Initialize components for Routine "Trial"
  TrialClock = new util.Clock();
  // Run 'Begin Experiment' code from omnicode
  // ─── Utility Functions ───────────────────────────────────────────────────────
  
  window.list = function(s) {
      if (typeof s === 'string') return s.split('');
      return s;
  };
  
  var _pj;
  function _pj_snippets(container) {
      function in_es6(left, right) {
          if (((right instanceof Array) || ((typeof right) === "string"))) {
              return (right.indexOf(left) > (- 1));
          } else {
              if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                  return right.has(left);
              } else {
                  return (left in right);
              }
          }
      }
      container["in_es6"] = in_es6;
      return container;
  }
  _pj = {};
  _pj_snippets(_pj);
  window._pj = _pj;
  
  window.safeFloat = function(value) {
      if (value === undefined || value === '' || value === 'x') return null;
      const num = parseFloat(value);
      return isNaN(num) ? undefined : num;
  };
  
  window.safeString = function(value) {
      if (value === undefined || value === null) return undefined;
  
      const str = String(value).trim();
  
      if (str === '' || str.toLowerCase() === 'nan' || str.toLowerCase() === 'x') {
          return undefined;
      }
  
      return str;  // DO NOT modify content
  };
  
  window.safeBool = function(value) {
      if (value === undefined || value === '' || value === 'x') return false;
      return String(value).trim().toLowerCase() === 'true';
  };
  
  window.safeTuple = function(value) {
      if (!value) return undefined;
  
      if (Array.isArray(value)) return value;
  
      const str = String(value).trim();
  
      if (str === "" || str === "-1") return undefined;
  
      // Strip surrounding parens if present, then split on semicolon
      const inner = str.replace(/^\(|\)$/g, '');
      const parts = inner.split(';').map(s => Number(s.trim()));
  
      if (parts.length < 2 || parts.some(isNaN)) return undefined;
  
      return [parts[0], parts[1]];
  };
  
  window.random_float = function(state = [undefined]) {
      return Math.random();
  };
  
  window.ln = function(x, tol = 1e-9) {
      if (x <= 0) throw new Error("ln undefined for x <= 0");
      if (x === 1) return 0.0;
      function exp_series(y) {
          if (y > 50) return 1e50;
          if (y < -50) return 1e-50;
          let term = 1.0, result = 1.0;
          for (let n = 1; n < 100; n++) {
              term *= (y / n);
              result += term;
              if (Math.abs(term) < 1e-15) break;
          }
          return result;
      }
      let [low, high] = x < 1 ? [-20.0, 0.0] : [0.0, 20.0];
      for (let i = 0; i < 100; i++) {
          if ((high - low) < tol) break;
          const mid = (low + high) / 2;
          exp_series(mid) < x ? (low = mid) : (high = mid);
      }
      return (low + high) / 2;
  };
  
  window.log_base = function(x, base, tol = 1e-9) {
      if (base <= 0 || base === 1) throw new Error("Base must be positive and not equal to 1");
      return window.ln(x, tol) / window.ln(base, tol);
  };
  
  window.random_normal = function(mu = 0.0, sigma = 1.0) {
      const u1 = Math.random(), u2 = Math.random();
      const z0 = Math.sqrt(-2.0 * Math.log(u1)) * Math.cos(2.0 * Math.PI * u2);
      return mu + sigma * z0;
  };
  
  window.random_exponential = function(scale = 1.0) {
      let u = Math.random();
      while (u === 0 || u === 1) u = Math.random();
      return -scale * Math.log(u);
  };
  
  window.random_permutation = function(n) {
      const arr = (typeof n === 'number') ? Array.from({length: n}, (_, i) => i) : [...n];
      for (let i = arr.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [arr[i], arr[j]] = [arr[j], arr[i]];
      }
      return arr;
  };
  
  window.choice = function(sequence) {
      return sequence[Math.floor(Math.random() * sequence.length)];
  };
  
  window.check_colors = function(color1, color2) {
      if (color1.length !== color2.length) return false;
      for (let i = 0; i < color1.length; i++) {
          if (color1[i] !== color2[i]) return false;
      }
      return true;
  };
  
  // ─── Clock & Sounds ──────────────────────────────────────────────────────────
  
  window.routine_clock = new util.Clock();
  window.reset_routine_clock = function() { window.routine_clock.reset(); };
  
  // ─── State Variables ─────────────────────────────────────────────────────────
  window.loop_type = 'sequential';
  window.used_schedules           = [];
  window.switch_enabled           = true;
  window.tab_pressed              = false;
  window.gl_flash                 = false;
  window.rl_flash                 = false;
  window.current_sound            = undefined;
  window.handle_blackout          = false;
  window.session_number           = 0;
  window.points                   = 0;
  window.press_blue_earn_index    = 0;
  window.press_blue_loss_index    = 0;
  window.press_yellow_earn_index  = 0;
  window.press_yellow_loss_index  = 0;
  window.blue_fh_index            = 0;
  window.yellow_fh_index          = 0;
  window.blue_pun_fh_index        = 0;
  window.yellow_pun_fh_index      = 0;
  window.blue_earn_proc_value     = 1;
  window.blue_loss_proc_value     = 1;
  window.yellow_earn_proc_value   = 1;
  window.yellow_loss_proc_value   = 1;
  window.blue_interval_earn_value   = random_float();
  window.yellow_interval_earn_value = random_float();
  window.blue_interval_loss_value   = random_float();
  window.yellow_interval_loss_value = random_float();
  window.in_changeover_delay      = false;
  window.current_schedule         = undefined;
  window.point_earned             = 0;
  
  // ─── Colors ──────────────────────────────────────────────────────────────────
  
  window.light_on      = [1, 1, 1];
  window.light_off     = [-1, -1, -1];
  window.button_color1 = [-1, -1, 1];
  window.button_color2 = [1, 1, -1];
  window.light_state   = "off";
  
  // ─── Visual Stimuli ──────────────────────────────────────────────────────────
  
  window.green_light = new visual.Rect({
      win: psychoJS.window, name: 'green_light', units: 'height',
      size: [0.2828, 0.2828], fillColor: [-1.0, -0.302, -1.0], colorSpace: 'rgb', pos: [-0.45, 0]
  });
  window.red_light = new visual.Rect({
      win: psychoJS.window, name: 'red_light', units:'height',
      size: [0.2828, 0.2828], fillColor: [-0.302, -1, -1.0], colorSpace: 'rgb', pos: [0.45, 0]
  });
  window.button_response = new visual.Rect({
      win: psychoJS.window, name: 'button_response', units: 'height', lineWidth: 3,
      size: [0.9192, 0.5657], fillColor: [-1, -1, 1], lineColor: new util.Color('grey'), colorSpace: 'rgb', pos: [0, 0], opacity: 1
  });
  window.button_cycle = new visual.Rect({
      win: psychoJS.window, name: 'button_cycle', units: 'height', depth: 1,
      size: [0.9192, 0.1414], fillColor: [0.6549, 0.6549, 0.6549], lineColor: [0, 0, 0], colorSpace: 'rgb', pos: [0, -0.3], opacity: 1
  });
  window.switch_text = new visual.TextStim({
      win: psychoJS.window, name: 'switch_text',
      text: 'Switch', height: 0.05, color: 'black',
      pos: [0, -0.3], opacity: 1, units: 'height', depth: -1  
  });
  window.points_display = new visual.TextStim({
      win: psychoJS.window, name: 'points_display',
      text: 'Points: 0', height: 0.05, color: [-1, -1, -1], pos: [0, 0.25]
  });
  window.response_bo = new visual.Rect({
      win: psychoJS.window, name: 'response_bo', units: 'height', lineColor: ['grey'], lineWidth: 3,
      size: [0.9192, 0.5657], fillColor: [0.6549, 0.6549, 0.6549], colorSpace: 'rgb', pos: [0, 0]
  });
  window.timer_text = new visual.TextStim({
      win: psychoJS.window, name: 'timer_text',
      text: 'Time Remaining: 15', height: 0.045, color: 'black', pos: [0, 0]
  });
  window.green_light_bo = new visual.Rect({
      win: psychoJS.window, name: 'green_light_bo', units: 'height',
      size: [0.2828, 0.2828], fillColor: [0.3339, 0.3339, 0.3339], colorSpace: 'rgb', pos: [-0.45, 0]
  });
  window.red_light_bo = new visual.Rect({
      win: psychoJS.window, name: 'red_light_bo', units: 'height',
      size: [0.2828, 0.2828], fillColor: [0.3339, 0.3339, 0.3339], colorSpace: 'rgb', pos: [0.45, 0]
  });
  window.button_cycle_bo = new visual.Rect({
      win: psychoJS.window, name: 'button_cycle_bo', units: 'height', size: [0.9192, 0.1414],
      fillColor: [0.4549, 0.4549, 0.4549], lineColor: [0, 0, 0], colorSpace: 'rgb', pos: [0, -0.3]
  });
  window.goodbye_message = new visual.TextStim({
      win: psychoJS.window, name: 'goodbye_message',
      text: "Thank you for completing the experiment. Your responses are recorded and you are free to leave.",
      height: 0.05, color: [1, 1, 1], pos: [0, 0]
  });
  
  // ─── Lights Array ─────────────────────────────────────────────────────────────
  
  window.lights = [];
  const light_positions = [-0.75,-0.6,-0.45,-0.3,-0.15,0,0.15,0.3,0.45,0.6,0.75];
  for (let i = 0; i < 11; i++) {
      window.lights.push(new visual.Rect({
          win: psychoJS.window, name: `light_${i+1}`, units: 'height',
          size: [0.177, 0.177], fillColor: window.light_off, colorSpace: 'rgb',
          pos: [light_positions[i], 0.4]
      }));
  }
  window.light_mapping = {};
  for (let i = 0; i < 11; i++) window.light_mapping[i+1] = window.lights[i];
  
  // ─── Classes ─────────────────────────────────────────────────────────────────
  
  window.ScheduleManager = class ScheduleManager {
      constructor(
          blue_i, yellow_i, blue_pun_i, yellow_pun_i,
          blue_r, yellow_r, blue_pun_r, yellow_pun_r,
          blue_random_i, yellow_random_i,
          blue_pun_random_i, yellow_pun_random_i,
          blue_random_r, yellow_random_r,
          blue_pun_random_r, yellow_pun_random_r,
          blue_fh, yellow_fh, blue_pun_fh, yellow_pun_fh,
          blue_fh_n_intervals, yellow_fh_n_intervals,
          blue_pun_fh_n_intervals, yellow_pun_fh_n_intervals,
          blue_fh_type, yellow_fh_type,
          blue_pun_fh_type, yellow_pun_fh_type,
          session_duration,
          blue_mag, yellow_mag,
          blue_pun_mag, yellow_pun_mag,
          changeover_delay, blackout_duration,
          blue_dist_type, yellow_dist_type,
          blue_pun_dist_type, yellow_pun_dist_type,
          sd_blue_interval, sd_yellow_interval,
          sd_blue_pun_interval, sd_yellow_pun_interval,
          schedule_lights,
          context_path, context_position, context_size,
          context_opacity, context_depth,
          ding_path, womp_path, keyboard_path
      ) {
  
          // Core schedules
          this.blue_i = blue_i || Infinity;
          this.yellow_i = yellow_i || Infinity;
          this.blue_pun_i = blue_pun_i || Infinity;
          this.yellow_pun_i = yellow_pun_i || Infinity;
  
          this.blue_r = blue_r || Infinity;
          this.yellow_r = yellow_r || Infinity;
          this.blue_pun_r = blue_pun_r || Infinity;
          this.yellow_pun_r = yellow_pun_r || Infinity;
          
          this.blue_random_i = blue_random_i || Infinity;
          this.yellow_random_i = yellow_random_i || Infinity;
          this.blue_pun_random_i = blue_pun_random_i || Infinity;
          this.yellow_pun_random_i = yellow_pun_random_i || Infinity;
  
          this.blue_random_r = blue_random_r || -Infinity;
          this.yellow_random_r = yellow_random_r || -Infinity;
          this.blue_pun_random_r = blue_pun_random_r || -Infinity;
          this.yellow_pun_random_r = yellow_pun_random_r || -Infinity;
          
          this.blue_fh = blue_fh;
          this.yellow_fh = yellow_fh;
          this.blue_pun_fh = blue_pun_fh;
          this.yellow_pun_fh = yellow_pun_fh;
  
          this.blue_fh_n_intervals = blue_fh_n_intervals || 0;
          this.yellow_fh_n_intervals = yellow_fh_n_intervals || 0;
          this.blue_pun_fh_n_intervals = blue_pun_fh_n_intervals || 0;
          this.yellow_pun_fh_n_intervals = yellow_pun_fh_n_intervals || 0;
  
          this.blue_fh_type = blue_fh_type || false;
          this.yellow_fh_type = yellow_fh_type || false;
          this.blue_pun_fh_type = blue_pun_fh_type || false;
          this.yellow_pun_fh_type = yellow_pun_fh_type || false;
          
          this.session_duration = session_duration || 1;
  
          this.blue_mag = blue_mag || 1;
          this.yellow_mag = yellow_mag || 1;
          this.blue_pun_mag = blue_pun_mag || 1;
          this.yellow_pun_mag = yellow_pun_mag || 1;
          
          this.changeover_delay = changeover_delay || 0;
          
          this.blackout_duration = blackout_duration || 5;
          
          this.blue_dist_type = blue_dist_type;
          this.yellow_dist_type = yellow_dist_type;
          this.blue_pun_dist_type = blue_pun_dist_type;
          this.yellow_pun_dist_type = yellow_pun_dist_type;
          
          this.sd_blue_interval = sd_blue_interval || 0;
          this.sd_yellow_interval = sd_yellow_interval || 0;
          this.sd_blue_pun_interval = sd_blue_pun_interval || 0;
          this.sd_yellow_pun_interval = sd_yellow_pun_interval || 0;
          
          this.schedule_lights = schedule_lights || "off";
  
          this.context_path =
          (typeof context_path === "string" && context_path !== "-1")
              ? context_path
              : null;
          this.context_position = context_position || [0, 0];
          this.context_size =
          (Array.isArray(context_size) && context_size.length === 2)
              ? context_size
              : [2, 2];
          this.context_opacity = context_opacity || 1;
          this.context_depth = context_depth || -1;
  
          this.ding_path =
              (typeof ding_path === "string" && ding_path !== "-1")
                  ? ding_path
                  : null;
  
          this.womp_path =
              (typeof womp_path === "string" && womp_path !== "-1")
                  ? womp_path
                  : null;
                  
          this.keyboard_path = keyboard_path || null;
  
          // FH tracking
          this.blue_fh_index = 0;
          this.yellow_fh_index = 0;
          this.blue_pun_fh_index = 0;
          this.yellow_pun_fh_index = 0;
  
          this.blue_fh_list = [];
          this.yellow_fh_list = [];
          this.blue_pun_fh_list = [];
          this.yellow_pun_fh_list = [];
  
          this.generate_fleshler_hoffman_list();
  
          // Timing
          this.next_blue_earn_time = 0;
          this.next_blue_loss_time = 0;
          this.next_yellow_earn_time = 0;
          this.next_yellow_loss_time = 0;
  
          this.last_switch_time = 0;
  
          this.interval_start = window.routine_clock.getTime();
          this.reset_times();
      }
  
      calculate_fleshler_hoffman(mean, n_intervals) {
          const e = Math.E;
          if (!mean || !n_intervals || n_intervals <= 0) return [0];
  
          n_intervals = parseInt(n_intervals);
          const intervals = [];
  
          for (let n = 1; n <= n_intervals; n++) {
              let tn;
              if (n === n_intervals) {
                  tn = mean * (1 + window.log_base(n_intervals, e));
              } else {
                  tn = mean * (
                      1 + window.log_base(n_intervals, e) +
                      (n_intervals - n) * window.log_base(n_intervals - n, e) -
                      (n_intervals - n + 1) * window.log_base(n_intervals - n + 1, e)
                  );
              }
              intervals.push(tn);
          }
          return intervals;
      }
  
      generate_fleshler_hoffman_list() {
          const process = (flag, i_val, r_val, n, type) => {
              if (!flag) return [Infinity];
  
              const value = (i_val > 0 && i_val !== Infinity) ? i_val : r_val;
              if (value <= 0 || value === Infinity) return [Infinity];
  
              const vals = this.calculate_fleshler_hoffman(value, n);
  
              try {
                  const t = type.toUpperCase();
                  if (t === "PROGRESSIVE") return [...vals].sort((a,b)=>a-b);
                  if (t === "REGRESSIVE") return [...vals].sort((a,b)=>b-a);
                  if (t === "RANDOM") return window.random_permutation(vals);
                  throw new Error("Invalid FH type");
              } catch {
                  return [Infinity];
              }
          };
  
          this.blue_fh_list       = process(this.blue_fh, this.blue_i, this.blue_r, this.blue_fh_n_intervals, this.blue_fh_type);
          this.yellow_fh_list     = process(this.yellow_fh, this.yellow_i, this.yellow_r, this.yellow_fh_n_intervals, this.yellow_fh_type);
          this.blue_pun_fh_list   = process(this.blue_pun_fh, this.blue_pun_i, this.blue_pun_r, this.blue_pun_fh_n_intervals, this.blue_pun_fh_type);
          this.yellow_pun_fh_list = process(this.yellow_pun_fh, this.yellow_pun_i, this.yellow_pun_r, this.yellow_pun_fh_n_intervals, this.yellow_pun_fh_type);
      }
  
      // ===== TIME-BASED =====
      calculate_next_blue_earn_time() {
          let interval;
  
          if (this.blue_fh && this.blue_i > 0 && this.blue_i !== Infinity) {
              interval = this.blue_fh_list[this.blue_fh_index % this.blue_fh_list.length];
          } else {
              interval = (this.blue_dist_type === "GAUSSIAN")
                  ? Math.max(window.random_normal(this.blue_random_i, this.sd_blue_interval), 0)
                  : window.random_exponential(this.blue_random_i);
          }
  
          return window.routine_clock.getTime() + interval;
      }
  
      calculate_next_yellow_earn_time() {
          let interval;
  
          if (this.yellow_fh && this.yellow_i > 0 && this.yellow_i !== Infinity) {
              interval = this.yellow_fh_list[this.yellow_fh_index % this.yellow_fh_list.length];
          } else {
              interval = (this.yellow_dist_type === "GAUSSIAN")
                  ? Math.max(window.random_normal(this.yellow_random_i, this.sd_yellow_interval), 0)
                  : window.random_exponential(this.yellow_random_i);
          }
  
          return window.routine_clock.getTime() + interval;
      }
  
      calculate_next_blue_loss_time() {
          let interval;
  
          if (this.blue_pun_fh && this.blue_pun_i > 0 && this.blue_pun_i !== Infinity) {
              interval = this.blue_pun_fh_list[this.blue_pun_fh_index % this.blue_pun_fh_list.length];
          } else {
              interval = (this.blue_pun_dist_type === "GAUSSIAN")
                  ? Math.max(window.random_normal(this.blue_pun_random_i, this.sd_blue_pun_interval), 0)
                  : window.random_exponential(this.blue_pun_random_i);
          }
  
          return window.routine_clock.getTime() + interval;
      }
  
      calculate_next_yellow_loss_time() {
          let interval;
  
          if (this.yellow_pun_fh && this.yellow_pun_i > 0 && this.yellow_pun_i !== Infinity) {
              interval = this.yellow_pun_fh_list[this.yellow_pun_fh_index % this.yellow_pun_fh_list.length];
          } else {
              interval = (this.yellow_pun_dist_type === "GAUSSIAN")
                  ? Math.max(window.random_normal(this.yellow_pun_random_i, this.sd_yellow_pun_interval), 0)
                  : window.random_exponential(this.yellow_pun_random_i);
          }
  
          return window.routine_clock.getTime() + interval;
      }
  
      reset_times() {
          window.reset_routine_clock();
          this.next_blue_earn_time   = this.calculate_next_blue_earn_time();
          this.next_yellow_earn_time = this.calculate_next_yellow_earn_time();
          this.next_blue_loss_time   = this.calculate_next_blue_loss_time();
          this.next_yellow_loss_time = this.calculate_next_yellow_loss_time();
      }
  };
  
  
  window.FlashManager = class FlashManager {
      constructor() {
          this.flash_states      = { gl: false, rl: false, switch_cod: false, rb: false, cycle: false };
          this.flash_start_times = { gl: 0,     rl: 0,     switch_cod: 0,     rb: 0,     cycle: 0     };
          this.flash_durations   = { gl: 0.25,  rl: 0.25,  switch_cod: 0.5,   rb: 0.1,   cycle: 0.1   };
      }
  
      start_flash(flash_type, start_time) {
          this.flash_states[flash_type] = true;
          this.flash_start_times[flash_type] = start_time;
      }
  
      update_flashes(current_time, green_light, red_light, button_response, button_cycle) {
  
          const safeFill = (stim, color) => {
              if (stim && typeof stim.setFillColor === "function") {
                  stim.setFillColor(color);
              }
          };
  
          const safeLine = (stim, color) => {
              if (stim && typeof stim.setLineColor === "function") {
                  stim.setLineColor(color);
              }
          };
  
          const safeDraw = (stim, val) => {
              if (stim && typeof stim.setAutoDraw === "function") {
                  stim.setAutoDraw(val);
              }
          };
  
          for (const flash_type of Object.keys(this.flash_states)) {
  
              if (!this.flash_states[flash_type]) continue;
  
              const elapsed = current_time - this.flash_start_times[flash_type];
  
              if (elapsed < this.flash_durations[flash_type]) {
  
                  if (flash_type === "gl") {
                      safeFill(green_light, [0.1294, 0.8667, 0.1294]);
                  }
  
                  else if (flash_type === "rl") {
                      safeFill(red_light, [0.8667, 0.1294, 0.1294]);
                  }
  
                  else if (flash_type === "rb") {
                      if (button_response && button_response.fillColor) {
  
                          const fill = button_response.fillColor;
  
                          const isColor = (a, b) =>
                              a && b && a[0] === b[0] && a[1] === b[1] && a[2] === b[2];
  
                          if (isColor(fill, button_color1)) {
                              safeLine(button_response, new util.Color('blue'));
                          } 
                          else if (isColor(fill, button_color2)) {
                              safeLine(button_response, new util.Color('yellow'));
                          } 
                          else {
                              safeLine(button_response, new util.Color('blue'));
                          }
                      }
                  }
  
                  else if (flash_type === "cycle") {
                      safeFill(button_cycle, [0.8549, 0.8549, 0.8549]);
                      safeDraw(window.switch_text, true);
                  }
  
              } else {
  
                  this.flash_states[flash_type] = false;
  
                  if (flash_type === "gl") {
                      safeFill(green_light, [-1.0, -0.302, -1.0]);
                  }
  
                  else if (flash_type === "rl") {
                      safeFill(red_light, [-0.302, -1.0, -1.0]);
                  }
  
                  else if (flash_type === "rb") {
                      safeLine(button_response, new util.Color('grey'));
                  }
  
                  else if (flash_type === "cycle") {
                      safeFill(button_cycle, [0.6549, 0.6549, 0.6549]);
                      safeDraw(window.switch_text, true);
                  }
              }
          }
      }
  };
  
  // ─── Top-Level Functions ─────────────────────────────────────────────────────
  window.get_new_schedule = function() {
      const available = [...new Set(window.all_schedules.filter(
          s => !window.used_schedules.includes(s)
      ))];
  
      if (available.length === 0) return null;
  
      let selected;
      // Guard: Selection_type may not be initialized yet on first call
      const method = (window.Selection_type && window.Selection_type.method) 
          ? window.Selection_type.method 
          : 'sequential';
  
      if (method === "random") {
          selected = window.choice(available);
      } else {
          available.sort();
          selected = available[0];
      }
  
      window.used_schedules.push(selected);
      return selected;
  };
  
  window.play_sound = function(sound_obj) {
      if (window.current_sound !== undefined && window.current_sound.status === sound.STARTED) {
          window.current_sound.stop();
      }
      sound_obj.play();
      return sound_obj;
  };
  
  window.handle_space_key = function (
      t,
      schedule_manager,
      flash_manager,
      points,
      button_response,
      press_blue_earn_index,
      press_blue_loss_index,
      press_yellow_earn_index,
      press_yellow_loss_index,
      sounds
  ) {
      let point_earned = 0;
  
      const ding = sounds ? sounds["ding"] : null;
      const womp = sounds ? sounds["womp"] : null;
  
      // --- SAFETY ---
      if (!button_response || !button_response.fillColor) {
          console.log("button_response not ready");
          return [
              points,
              point_earned,
              press_blue_earn_index,
              press_blue_loss_index,
              press_yellow_earn_index,
              press_yellow_loss_index
          ];
      }
  
      const isBlue = window.check_colors(button_response.fillColor, window.button_color1);
      const isYellow = window.check_colors(button_response.fillColor, window.button_color2);
  
      const nearEnd = (schedule_manager.session_duration - t) > 0.3;
  
      // =====================
      // BLUE
      // =====================
      if (isBlue) {
  
          // Interval
          if (
              (0 < schedule_manager.blue_i && schedule_manager.blue_i < Infinity) ||
              (0 < schedule_manager.blue_random_i && schedule_manager.blue_random_i < Infinity)
          ) {
              if (t >= schedule_manager.next_blue_earn_time) {
                  points += parseInt(schedule_manager.blue_mag);
                  point_earned = 1;
  
                  schedule_manager.blue_fh_index += 1;
                  schedule_manager.next_blue_earn_time =
                      schedule_manager.calculate_next_blue_earn_time();
  
                  if (nearEnd) {
                      flash_manager.start_flash("gl", t);
                      if (ding) window.play_sound(ding);
                  }
              }
          }
  
          // Ratio
          else if (
              (0 < schedule_manager.blue_r && schedule_manager.blue_r < Infinity) ||
              (0 < schedule_manager.blue_random_r && schedule_manager.blue_random_r < Infinity)
          ) {
              press_blue_earn_index++;
  
              if (press_blue_earn_index >= Math.round(schedule_manager.calculate_next_press_earn_requirement(button_response))) {
                  points += parseInt(schedule_manager.blue_mag);
                  point_earned = 1;
  
                  press_blue_earn_index = 0;
                  schedule_manager.blue_fh_index += 1;
  
                  if (nearEnd) {
                      flash_manager.start_flash("gl", t);
                      if (ding) window.play_sound(ding);
                  }
              }
          }
  
          // Punishment interval
          if (
              (0 < schedule_manager.blue_pun_i && schedule_manager.blue_pun_i < Infinity) ||
              (0 < schedule_manager.blue_pun_random_i && schedule_manager.blue_pun_random_i < Infinity)
          ) {
              if (t >= schedule_manager.next_blue_loss_time) {
                  points -= parseInt(schedule_manager.blue_pun_mag);
                  point_earned = -1;
  
                  schedule_manager.blue_pun_fh_index += 1;
                  schedule_manager.next_blue_loss_time =
                      schedule_manager.calculate_next_blue_loss_time();
  
                  if (nearEnd) {
                      flash_manager.start_flash("rl", t);
                      if (womp) window.play_sound(womp);
                  }
              }
          }
  
          // Punishment ratio
          else if (
              (0 < schedule_manager.blue_pun_r && schedule_manager.blue_pun_r < Infinity) ||
              (0 < schedule_manager.blue_pun_random_r && schedule_manager.blue_pun_random_r < Infinity)
          ) {
              press_blue_loss_index++;
  
              if (press_blue_loss_index >= Math.round(schedule_manager.calculate_next_press_loss_requirement(button_response))) {
                  points -= parseInt(schedule_manager.blue_pun_mag);
                  point_earned = -1;
  
                  press_blue_loss_index = 0;
                  schedule_manager.blue_pun_fh_index += 1;
  
                  if (nearEnd) {
                      flash_manager.start_flash("rl", t);
                      if (womp) window.play_sound(womp);
                  }
              }
          }
      }
  
      // =====================
      // YELLOW
      // =====================
      if (isYellow) {
  
          // Interval
          if (
              (0 < schedule_manager.yellow_i && schedule_manager.yellow_i < Infinity) ||
              (0 < schedule_manager.yellow_random_i && schedule_manager.yellow_random_i < Infinity)
          ) {
              if (t >= schedule_manager.next_yellow_earn_time) {
                  points += parseInt(schedule_manager.yellow_mag);
                  point_earned = 1;
  
                  schedule_manager.yellow_fh_index += 1;
                  schedule_manager.next_yellow_earn_time =
                      schedule_manager.calculate_next_yellow_earn_time();
  
                  if (nearEnd) {
                      flash_manager.start_flash("gl", t);
                      if (ding) window.play_sound(ding);
                  }
              }
          }
  
          // Ratio
          else if (
              (0 < schedule_manager.yellow_r && schedule_manager.yellow_r < Infinity) ||
              (0 < schedule_manager.yellow_random_r && schedule_manager.yellow_random_r < Infinity)
          ) {
              press_yellow_earn_index++;
  
              if (press_yellow_earn_index >= Math.round(schedule_manager.calculate_next_press_earn_requirement(button_response))) {
                  points += parseInt(schedule_manager.yellow_mag);
                  point_earned = 1;
  
                  press_yellow_earn_index = 0;
                  schedule_manager.yellow_fh_index += 1;
  
                  if (nearEnd) {
                      flash_manager.start_flash("gl", t);
                      if (ding) window.play_sound(ding);
                  }
              }
          }
  
          // Punishment interval
          if (
              (0 < schedule_manager.yellow_pun_i && schedule_manager.yellow_pun_i < Infinity) ||
              (0 < schedule_manager.yellow_pun_random_i && schedule_manager.yellow_pun_random_i < Infinity)
          ) {
              if (t >= schedule_manager.next_yellow_loss_time) {
                  points -= parseInt(schedule_manager.yellow_pun_mag);
                  point_earned = -1;
  
                  schedule_manager.yellow_pun_fh_index += 1;
                  schedule_manager.next_yellow_loss_time =
                      schedule_manager.calculate_next_yellow_loss_time();
  
                  if (nearEnd) {
                      flash_manager.start_flash("rl", t);
                      if (womp) window.play_sound(womp);
                  }
              }
          }
  
          // Punishment ratio
          else if (
              (0 < schedule_manager.yellow_pun_r && schedule_manager.yellow_pun_r < Infinity) ||
              (0 < schedule_manager.yellow_pun_random_r && schedule_manager.yellow_pun_random_r < Infinity)
          ) {
              press_yellow_loss_index++;
  
              if (press_yellow_loss_index >= Math.round(schedule_manager.calculate_next_press_loss_requirement(button_response))) {
                  points -= parseInt(schedule_manager.yellow_pun_mag);
                  point_earned = -1;
  
                  press_yellow_loss_index = 0;
                  schedule_manager.yellow_pun_fh_index += 1;
  
                  if (nearEnd) {
                      flash_manager.start_flash("rl", t);
                      if (womp) window.play_sound(womp);
                  }
              }
          }
      }
  
      return [
          points,
          point_earned,
          press_blue_earn_index,
          press_blue_loss_index,
          press_yellow_earn_index,
          press_yellow_loss_index
      ];
  };
  
  window.collect_space = function() {
      psychoJS.experiment.addData("SessionNumber", `#${window.session_number}`);
      psychoJS.experiment.addData("Time", window.t);
      psychoJS.experiment.addData("Points", window.points);
      psychoJS.experiment.addData("Point Earned", window.point_earned);
      psychoJS.experiment.addData("During Changeover?", window.in_changeover_delay);
      psychoJS.experiment.addData("CurrentSchedule", window.current_schedule);
      psychoJS.experiment.addData("Button", window.check_colors(window.button_response.fillColor, window.button_color1) ? "Blue" : "Yellow");
      psychoJS.experiment.nextEntry();
  };
  
  window.handle_tab_key = function(t, flash_manager) {
      flash_manager.start_flash("cycle", t);
      if (window.check_colors(window.button_response.fillColor, window.button_color1)) {
          window.button_response.fillColor = window.button_color2;
      } else {
          window.button_response.fillColor = window.button_color1;
      }
      window.schedule_manager.last_switch_time = t;
      return false;
  };
  
  window.collect_tab = function() {
      psychoJS.experiment.addData("SessionNumber", `#${window.session_number}`);
      psychoJS.experiment.addData("Time", window.t);
      psychoJS.experiment.addData("Points", window.points);
      psychoJS.experiment.addData("Point Earned", "N/A");
      psychoJS.experiment.addData("During Changeover?", window.in_changeover_delay);
      psychoJS.experiment.addData("CurrentSchedule", window.current_schedule);
      psychoJS.experiment.addData("Button", "Tab");
      psychoJS.experiment.nextEntry();
  };
  
  window.draw_main = function(schedule_manager, context_image) {
      // Turn OFF blackout stimuli
      window.green_light_bo.setAutoDraw(false);
      window.red_light_bo.setAutoDraw(false);
      window.response_bo.setAutoDraw(false);
      window.button_cycle_bo.setAutoDraw(false);
      window.timer_text.setAutoDraw(false);
  
      if (window.context_image) window.context_image.draw();
   
      if (window.lights && window.lights.length > 0) {
          if (schedule_manager.schedule_lights.toLowerCase() === "on") {
              const total = window.all_schedules.length;
              const spacing = 0.15;
              const start = (total % 2 === 0)
                  ? -(total/2 - 0.5) * spacing
                  : -Math.floor(total/2) * spacing;
              for (let i = 0; i < window.lights.length; i++) {
                  const light = window.lights[i];
                  if (i < total) {
                      light.setAutoDraw(true);
                      light.pos = [start + i * spacing, 0.4];
                      light.setFillColor(
                          (i + 1) === parseInt(window.current_schedule)
                              ? window.light_on
                              : window.light_off,
                          'rgb'
                      );
                  } else {
                      light.setAutoDraw(false);
                  }
              }
          } else {
              for (let i = 0; i < window.lights.length; i++) {
                  window.lights[i].setAutoDraw(false);
              }
          }
      }
  
      window.green_light.setAutoDraw(true);
      window.red_light.setAutoDraw(true);
      window.button_response.setAutoDraw(true);
      window.button_cycle.setAutoDraw(true);
      window.points_display.setAutoDraw(true);
      window.switch_text.setAutoDraw(true);
  };
  
  window.draw_break = function() {
  
      // Turn OFF main stimuli ONLY
      window.green_light.setAutoDraw(false);
      window.red_light.setAutoDraw(false);
      window.button_response.setAutoDraw(false);
      window.button_cycle.setAutoDraw(false);
  
      if (window.lights) {
          for (let light of window.lights) {
              light.setAutoDraw(false);
          }
      }
  
      // Turn ON blackout stimuli
      window.green_light_bo.setAutoDraw(true);
      window.red_light_bo.setAutoDraw(true);
      window.points_display.setAutoDraw(true);
      window.response_bo.setAutoDraw(true);
      window.button_cycle_bo.setAutoDraw(true);
      window.timer_text.setAutoDraw(true);
  };
  
  window.handle_blackout_period = function(blackout_timer) { 
      const remaining = Math.max(0, Math.floor(blackout_timer.getTime()));
  
      const end_keys = psychoJS.eventManager.getKeys(["escape"]);
      if (end_keys.includes("escape")) { 
          psychoJS.quit(); 
          return false; 
      }
  
      if (remaining > 0) {
          window.timer_text.text = `Time Remaining: ${remaining}`;
          window.draw_break();
          return false;
      }
  
      window.timer_text.text = "Hit 'enter' to continue";
      window.draw_break();
  
      if (window.read_keys.includes("return")) {
          console.log("BLACKOUT COMPLETE TRIGGERED");
          return true;
      }
  
      return false;
  };
  
  window.initialize_trial_stim = function(schedule_manager) {
      if (window.context_image) window.context_image.setAutoDraw(true);
      window.green_light.setAutoDraw(true);
      window.red_light.setAutoDraw(true);
      window.button_response.setAutoDraw(true);
      window.button_cycle.setAutoDraw(true);
      window.switch_text.setAutoDraw(true);
      window.points_display.setAutoDraw(true);
  
      if (window.lights != null) {
          for (let light of window.lights) {
              light.setAutoDraw(true);
          }
      }
  };
      
  window.initialize_blackout_stim = function() {
      window.green_light_bo.draw();
      window.red_light_bo.draw(); 
      window.points_display.draw(); 
      window.response_bo.draw(); 
      window.button_cycle_bo.draw(); 
      window.timer_text.draw();
  };
  
  window.hide_main_stim = function() {
      if (window.context_image) window.context_image.setAutoDraw(false);
      window.green_light.setAutoDraw(false);
      window.red_light.setAutoDraw(false);
      window.button_response.setAutoDraw(false);
      window.button_cycle.setAutoDraw(false);
  
      if (window.lights != null) {
          for (let light of window.lights) {
              light.setAutoDraw(false);
          }
      }
  };
  
  window.clear_all_stim = function() {
      
      if (window.context_image) window.context_image.setAutoDraw(false);
      window.green_light.setAutoDraw(false);
      window.red_light.setAutoDraw(false);
      window.button_response.setAutoDraw(false);
      window.button_cycle.setAutoDraw(false);
      window.switch_text.setAutoDraw(false);
  
      window.green_light_bo.setAutoDraw(false);
      window.red_light_bo.setAutoDraw(false);
      window.response_bo.setAutoDraw(false);
      window.button_cycle_bo.setAutoDraw(false);
      window.timer_text.setAutoDraw(false);
  
      if (window.lights != null) {
          for (let light of window.lights) {
              light.setAutoDraw(false);
          }
      }
  };
  
  window.preload_contexts = function(schedule_df) {
      const context_cache = {};
      schedule_df.forEach(row => {
          const schedule = String(window.safeString(row["Schedule_number"])).trim();
          const rawPath = row["Context_Path"];
          const path = window.safeString(rawPath);
          if (!path || typeof path !== "string") {
              console.log("Invalid context path for schedule:", schedule, rawPath);
              context_cache[schedule] = null;
              return;
          }
          const resource = psychoJS.serverManager.getResource(path);
          if (!resource) {
              console.error("RESOURCE NOT FOUND at preload:", path);
              context_cache[schedule] = null;
              return;
          }
          let pos = window.safeTuple(row["Context_Position"]);
          let size = window.safeTuple(row["Context_Size"]);
          let opacity = window.safeFloat(row["Context_Opacity"]);
          let depth = window.safeFloat(row["Context_Depth"]);
          if (isNaN(opacity)) opacity = 1;
          if (isNaN(depth)) depth = -1;
  
          // Build the ImageStim once here, reuse forever
          context_cache[schedule] = new visual.ImageStim({
              win: psychoJS.window,
              name: `context_${schedule}`,
              image: resource,
              pos: pos,
              size: size,
              opacity: opacity,
              depth: depth,
              autoDraw: false
          });
          console.log("Preloaded context for schedule:", schedule);
      });
      return context_cache;
  };
  
  window.get_context = function() {
      const key = String(window.current_schedule).trim();
      const stim = window.context_cache[key];
      if (!stim) {
          console.log("No context for schedule:", key);
          return null;
      }
      return stim;
  };
  
  window.sounds = {
      ding: new sound.Sound({
          win: psychoJS.window,
          value: 'stimuli/ding.wav'
      }),
      womp: new sound.Sound({
          win: psychoJS.window,
          value: 'stimuli/ha.wav'
      })
  };
  
  window.context_cache = window.preload_contexts(window.schedule_df);
  
  (window.button_response.fillColor === button_color1);
  // Initialize components for Routine "Goodbye"
  GoodbyeClock = new util.Clock();
  // Run 'Begin Experiment' code from goodbye
  window.draw_goodbye = function() {
      window.goodbye_message.draw();
  };
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function WelcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Welcome' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    WelcomeClock.reset();
    routineTimer.reset();
    WelcomeMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from welcome_and_data_collection
    psychoJS.eventManager.clearEvents();
    welcome = true;
    
    
    WelcomeMaxDuration = null
    // keep track of which components have finished
    WelcomeComponents = [];
    
    WelcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function WelcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Welcome' ---
    // get current time
    t = WelcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from welcome_and_data_collection
    // Schedule.Event is used to nullify PsychoJS
    // default settings. This is important for ease of 
    // use.
    
    continueRoutine = true;
    
    window.welcome_message.draw();
    
    // Enables the reading of keys
    window.read_keys = psychoJS.eventManager.getKeys();
    
    // Allow the user to withdraw consent 
    if (window.read_keys.includes("escape")) {
        psychoJS.quit({ message: "Experiment ended by participant." });
    }
    
    if (window.read_keys.includes("Tab")) {
        console.log("PsychoJS can read tab");
    }
    
    if (window.read_keys.includes("ctrl")) {
        console.log("PsychoJS can read ctrl");
    }
    
    if (window.read_keys.includes("shift")) {
        console.log("PsychoJS can read shift");
    }
    
    if (window.read_keys.includes("s")) {
        console.log("PsychoJS can read s");
    }
    
    // Procede to next routine
    
    if (window.read_keys.includes("return")) {
        console.log("Welcome ended with enter, huzzah!")
        return Scheduler.Event.NEXT;  
    }
    
    return Scheduler.Event.FLIP_REPEAT;
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    WelcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function WelcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Welcome' ---
    WelcomeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    console.log("Exited exit from welcome recorded");
    window.welcome_message.setAutoDraw(false);
    // the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function Selection_typeLoopBegin(Selection_typeLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Selection_type = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'Selection_type'
    });
    psychoJS.experiment.addLoop(Selection_type); // add the loop to the experiment
    currentLoop = Selection_type;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    Selection_type.forEach(function() {
      snapshot = Selection_type.getSnapshot();
    
      Selection_typeLoopScheduler.add(importConditions(snapshot));
      Selection_typeLoopScheduler.add(TrialRoutineBegin(snapshot));
      Selection_typeLoopScheduler.add(TrialRoutineEachFrame());
      Selection_typeLoopScheduler.add(TrialRoutineEnd(snapshot));
      Selection_typeLoopScheduler.add(Selection_typeLoopEndIteration(Selection_typeLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function Selection_typeLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(Selection_type);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function Selection_typeLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function TrialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Trial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    TrialClock.reset();
    routineTimer.reset();
    TrialMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from omnicode
    if (typeof Selection_type !== 'undefined' && window.loop_type === 'sequential') {
        window.loop_type = Selection_type.method;
        console.log("Loop type raw:", JSON.stringify(window.loop_type));
        console.log("Is random?", window.loop_type === TrialHandler.Method.RANDOM);
    }
    
    window.flash_manager = new window.FlashManager();
    window.routine_clock = new util.Clock();
    window.routine_clock.reset();
    window.routine_active = true;
    window.switch_enabled = true;
    window.tab_pressed = false;
    window.continue_routine = true;
    window.current_sound = undefined;
    window.transition_to_extinction = false;
    window.extinction = false;
    window.in_blackout = false;
    window.press_blue_earn_index = 0;
    window.press_blue_loss_index = 0;
    window.press_yellow_earn_index = 0;
    window.press_yellow_loss_index = 0;
    window.blue_earn_proc_value = 1;
    window.blue_loss_proc_value = 1;
    window.yellow_earn_proc_value = 1;
    window.yellow_loss_proc_value = 1;
    window.session_number += 1;
    
    window.available_schedules = Array.from(new Set(
        window.all_schedules.filter(x => !window.used_schedules.includes(x))
    ));
    
    window.current_schedule = window.get_new_schedule();
    
    if (window.current_schedule === undefined) {
        console.error('No available schedules remaining');
        window.continue_routine = false;
        window.schedule_loaded = false;
    } else {
        try {
            console.log(`Loading schedule: ${window.current_schedule}`);
    
            const schedule_data = window.schedule_df.find(
                row => row['Schedule_number'] == window.current_schedule
            );
    
            window.schedule_manager = new window.ScheduleManager(
                window.safeFloat(schedule_data['Blue_Interval']),
                window.safeFloat(schedule_data['Yellow_Interval']),
                window.safeFloat(schedule_data['Blue_Pun_Interval']),
                window.safeFloat(schedule_data['Yellow_Pun_Interval']),
                window.safeFloat(schedule_data['Blue_Ratio']),
                window.safeFloat(schedule_data['Yellow_Ratio']),
                window.safeFloat(schedule_data['Blue_Pun_Ratio']),
                window.safeFloat(schedule_data['Yellow_Pun_Ratio']),
                window.safeFloat(schedule_data['Blue_Random_Interval']),
                window.safeFloat(schedule_data['Yellow_Random_Interval']),
                window.safeFloat(schedule_data['Blue_Pun_Random_Interval']),
                window.safeFloat(schedule_data['Yellow_Pun_Random_Interval']),
                window.safeFloat(schedule_data['Blue_Random_Ratio']),
                window.safeFloat(schedule_data['Yellow_Random_Ratio']),
                window.safeFloat(schedule_data['Blue_Pun_Random_Ratio']),
                window.safeFloat(schedule_data['Yellow_Pun_Random_Ratio']),
                window.safeBool(schedule_data['Blue_FH']),
                window.safeBool(schedule_data['Yellow_FH']),
                window.safeBool(schedule_data['Blue_Pun_FH']),
                window.safeBool(schedule_data['Yellow_Pun_FH']),
                window.safeFloat(schedule_data['Blue_FH_Intervals']),
                window.safeFloat(schedule_data['Yellow_FH_Intervals']),
                window.safeFloat(schedule_data['Blue_Pun_FH_Intervals']),
                window.safeFloat(schedule_data['Yellow_Pun_FH_Intervals']),
                window.safeString(schedule_data['Blue_FH_Type']),
                window.safeString(schedule_data['Yellow_FH_Type']),
                window.safeString(schedule_data['Blue_Pun_FH_Type']),
                window.safeString(schedule_data['Yellow_Pun_FH_Type']),
                window.safeFloat(schedule_data['Session_Duration']),
                window.safeFloat(schedule_data['Blue_Mag']),
                window.safeFloat(schedule_data['Yellow_Mag']),
                window.safeFloat(schedule_data['Blue_Pun_Mag']),
                window.safeFloat(schedule_data['Yellow_Pun_Mag']),
                window.safeFloat(schedule_data['Changeover_Delay']),
                window.safeFloat(schedule_data['Blackout_Duration']),
                window.safeString(schedule_data['Blue_Distribution']),
                window.safeString(schedule_data['Yellow_Distribution']),
                window.safeString(schedule_data['Blue_Pun_Distribution']),
                window.safeString(schedule_data['Yellow_Pun_Distribution']),
                window.safeFloat(schedule_data['SD_Blue']),
                window.safeFloat(schedule_data['SD_Yellow']),
                window.safeFloat(schedule_data['SD_Blue_Pun']),
                window.safeFloat(schedule_data['SD_Yellow_Pun']),
                window.safeString(schedule_data['Schedule_Lights']),
                window.safeString(schedule_data['Context_Path']),
                window.safeTuple(schedule_data['Context_Position']),
                window.safeTuple(schedule_data['Context_Size']),
                window.safeFloat(schedule_data['Context_Opacity']),
                window.safeFloat(schedule_data['Context_Depth']),
                window.safeString(schedule_data['Ding_Path']),
                window.safeString(schedule_data['Womp_Path']),
                window.safeString(schedule_data['Keyboard_Path'])
                );
    
            window.schedule_loaded = true;
            window.schedule_manager.reset_times();
            window.blackout_timer = new util.CountdownTimer(window.schedule_manager.blackout_duration + 1);
            
            console.log(`Light status: ${window.lights}`);
    
            window.context_image = window.get_context(window.context_cache, window.current_schedule);  
            
            console.log(`First schedule: ${window.current_schedule}`);
    
            window.schedule_manager.calculate_next_yellow_earn_time();
            window.schedule_manager.generate_fleshler_hoffman_list();
    
            console.log(`Blue_FH: ${window.schedule_manager.blue_fh_list}`);
            console.log(`Yellow_FH: ${window.schedule_manager.yellow_fh_list}`);
            
            window.initialize_blackout_stim();     
            window.initialize_trial_stim(window.schedule_manager);
            
            window.routine_active = true;
            window.continue_routine = true;
    
        } catch (error) {
            console.error('Error loading schedule:', error);
            window.schedule_loaded = false;
            window.continue_routine = false;
        }
    }
    psychoJS.experiment.addData('Trial.started', globalClock.getTime());
    TrialMaxDuration = null
    // keep track of which components have finished
    TrialComponents = [];
    
    TrialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function TrialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Trial' ---
    // get current time
    t = TrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from omnicode
    continueRoutine = true;
    
    window.read_keys = psychoJS.eventManager.getKeys();
    
    if (window.read_keys.includes('escape')) {
        psychoJS.quit();
    }
    
    if (typeof window.schedule_df === 'undefined' || typeof window.all_schedules === 'undefined') {
        console.log("Window is undefined");
    } else {
    
        //Routine is active
        if (window.routine_active) {
    
            window.t = window.routine_clock.getTime();
            window.in_changeover_delay =
                (window.t - window.schedule_manager.last_switch_time < window.schedule_manager.changeover_delay);
    
            if (window.in_changeover_delay && window.read_keys.includes('s')) {
                window.read_keys.splice(window.read_keys.indexOf('s'), 1);
                window.collect_tab();
            }
    
            window.tab_pressed = window.read_keys.includes('s');
    
            if (window.read_keys.includes('space')) {
                window.flash_manager.start_flash('rb', window.t, window.button_response);
    
                if (!window.in_changeover_delay) {
                    [
                        window.points,
                        window.point_earned,
                        window.press_blue_earn_index,
                        window.press_blue_loss_index,
                        window.press_yellow_earn_index,
                        window.press_yellow_loss_index
                    ] = window.handle_space_key(
                        window.t,
                        window.schedule_manager,
                        window.flash_manager,
                        window.points,
                        window.button_response,
                        window.press_blue_earn_index,
                        window.press_blue_loss_index,
                        window.press_yellow_earn_index,
                        window.press_yellow_loss_index,
                        window.sounds
                    );
                    window.points_display.text = `Points: ${window.points}`;
                    window.collect_space();
                } else {
                    window.collect_space();
                }
            }
           
            if (window.tab_pressed && !window.in_changeover_delay) {
                window.switch_enabled = window.handle_tab_key(window.t, window.flash_manager);
                window.collect_tab();
            }
    
            window.flash_manager.update_flashes(
                window.t,
                window.green_light,
                window.red_light,
                window.button_response,
                window.button_cycle
            );
    
            window.draw_main(window.schedule_manager);
    
            //Start blackout
            if (window.routine_active && window.t >= window.schedule_manager.session_duration) {
                console.log("Session ended → starting blackout");
    
                window.routine_active = false;
    
                if (!window.in_blackout) {
                    window.blackout_timer.reset();
                    window.initialize_blackout_stim();
                    window.in_blackout = true;
                }
            }
    
        } else {
            
            window.hide_main_stim();
            let blackout_complete = window.handle_blackout_period(window.blackout_timer);
    
            if (blackout_complete) {
    
                window.in_blackout = false;
                if (window.all_schedules.length > window.used_schedules.length) {
    
                    console.log("schedule grabbed");
    
                    window.current_schedule = window.get_new_schedule();
    
                    const schedule_data = window.schedule_df.find(
                        row => row['Schedule_number'] == window.current_schedule
                    );
    
                    window.schedule_manager = new window.ScheduleManager(
                        window.safeFloat(schedule_data['Blue_Interval']),
                        window.safeFloat(schedule_data['Yellow_Interval']),
                        window.safeFloat(schedule_data['Blue_Pun_Interval']),
                        window.safeFloat(schedule_data['Yellow_Pun_Interval']),
                        window.safeFloat(schedule_data['Blue_Ratio']),
                        window.safeFloat(schedule_data['Yellow_Ratio']),
                        window.safeFloat(schedule_data['Blue_Pun_Ratio']),
                        window.safeFloat(schedule_data['Yellow_Pun_Ratio']),
                        window.safeFloat(schedule_data['Blue_Random_Interval']),
                        window.safeFloat(schedule_data['Yellow_Random_Interval']),
                        window.safeFloat(schedule_data['Blue_Pun_Random_Interval']),
                        window.safeFloat(schedule_data['Yellow_Pun_Random_Interval']),
                        window.safeFloat(schedule_data['Blue_Random_Ratio']),
                        window.safeFloat(schedule_data['Yellow_Random_Ratio']),
                        window.safeFloat(schedule_data['Blue_Pun_Random_Ratio']),
                        window.safeFloat(schedule_data['Yellow_Pun_Random_Ratio']),
                        window.safeBool(schedule_data['Blue_FH']),
                        window.safeBool(schedule_data['Yellow_FH']),
                        window.safeBool(schedule_data['Blue_Pun_FH']),
                        window.safeBool(schedule_data['Yellow_Pun_FH']),
                        window.safeFloat(schedule_data['Blue_FH_Intervals']),
                        window.safeFloat(schedule_data['Yellow_FH_Intervals']),
                        window.safeFloat(schedule_data['Blue_Pun_FH_Intervals']),
                        window.safeFloat(schedule_data['Yellow_Pun_FH_Intervals']),
                        window.safeString(schedule_data['Blue_FH_Type']),
                        window.safeString(schedule_data['Yellow_FH_Type']),
                        window.safeString(schedule_data['Blue_Pun_FH_Type']),
                        window.safeString(schedule_data['Yellow_Pun_FH_Type']),
                        window.safeFloat(schedule_data['Session_Duration']),
                        window.safeFloat(schedule_data['Blue_Mag']),
                        window.safeFloat(schedule_data['Yellow_Mag']),
                        window.safeFloat(schedule_data['Blue_Pun_Mag']),
                        window.safeFloat(schedule_data['Yellow_Pun_Mag']),
                        window.safeFloat(schedule_data['Changeover_Delay']),
                        window.safeFloat(schedule_data['Blackout_Duration']),
                        window.safeString(schedule_data['Blue_Distribution']),
                        window.safeString(schedule_data['Yellow_Distribution']),
                        window.safeString(schedule_data['Blue_Pun_Distribution']),
                        window.safeString(schedule_data['Yellow_Pun_Distribution']),
                        window.safeFloat(schedule_data['SD_Blue']),
                        window.safeFloat(schedule_data['SD_Yellow']),
                        window.safeFloat(schedule_data['SD_Blue_Pun']),
                        window.safeFloat(schedule_data['SD_Yellow_Pun']),
                        window.safeString(schedule_data['Schedule_Lights']),
                        window.safeString(schedule_data['Context_Path']),
                        window.safeTuple(schedule_data['Context_Position']),
                        window.safeTuple(schedule_data['Context_Size']),
                        window.safeFloat(schedule_data['Context_Opacity']),
                        window.safeFloat(schedule_data['Context_Depth']),
                        window.safeString(schedule_data['Ding_Path']),
                        window.safeString(schedule_data['Womp_Path']),
                        window.safeString(schedule_data['Keyboard_Path'])
                    );
    
                    //Reset everything
                    window.routine_clock.reset();
                    window.press_blue_earn_index = window.press_blue_loss_index = 0;
                    window.press_yellow_earn_index = window.press_yellow_loss_index = 0;
                    window.blue_earn_proc_value = window.blue_loss_proc_value = 1;
                    window.yellow_earn_proc_value = window.yellow_loss_proc_value = 1;
                    window.blue_fh_index = window.yellow_fh_index = 0;
                    window.blue_pun_fh_index = window.yellow_pun_fh_index = 0;
                    window.schedule_manager.interval_start = 0;
                    window.context_image = window.get_context(window.context_cache, window.current_schedule);  
    
                    psychoJS.eventManager.clearEvents();
    
                    window.session_number += 1;
    
                    console.log(window.current_schedule);
                    console.log(`Blue_FH: ${window.schedule_manager.blue_fh_list}`);
                    console.log(`Yellow_FH: ${window.schedule_manager.yellow_fh_list}`);
    
                    window.initialize_trial_stim(window.schedule_manager);
    
                    window.routine_active = true;
    
                } else {
                    continueRoutine = false;
                    return Scheduler.Event.NEXT; 
                }
            }
        }
    }
    
    return Scheduler.Event.FLIP_REPEAT;
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    TrialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function TrialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Trial' ---
    TrialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Trial.stopped', globalClock.getTime());
    // Run 'End Routine' code from omnicode
    window.all_schedules = window.schedule_df
        .map(row => row['Schedule_number'])
        .filter(s => s !== 'EXT' && s !== 'ACQ' && s !== 'Tutorial' && s !== 'Keyboard_Tutorial');
    console.log(window.all_schedules);
    console.log(`number of initial schedules: ${window.all_schedules.length}`);
    window.used_schedules = [];
    psychoJS.eventManager.clearEvents();
    window.clear_all_stim()
    // the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function GoodbyeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Goodbye' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    GoodbyeClock.reset();
    routineTimer.reset();
    GoodbyeMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from goodbye
    psychoJS.eventManager.clearEvents();
    window.goodbye = true;
    psychoJS.experiment.addData('Goodbye.started', globalClock.getTime());
    GoodbyeMaxDuration = null
    // keep track of which components have finished
    GoodbyeComponents = [];
    
    GoodbyeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function GoodbyeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Goodbye' ---
    // get current time
    t = GoodbyeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from goodbye
    continueRoutine = true;
    
    window.goodbye_message.draw();
    
    window.end_keys = psychoJS.eventManager.getKeys({ keyList: ["return"] });
    
    if (window.end_keys.includes("return")) {
        continueRoutine = false;
        return Scheduler.Event.NEXT;
    }
    
    return Scheduler.Event.FLIP_REPEAT;
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    GoodbyeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function GoodbyeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Goodbye' ---
    GoodbyeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Goodbye.stopped', globalClock.getTime());
    // the Routine "Goodbye" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  fetch('http://localhost:PORT/stop', { method: 'POST' }).catch(() => {});
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
