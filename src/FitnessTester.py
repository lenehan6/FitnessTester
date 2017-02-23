## enums
UNITS_SECONDS = 0;
UNITS_METERS = 1;

SCORE_TYPE_INDENTIFY = 0;
SCORE_TYPE_RUNSTART = 1;
SCORE_TYPE_RUNEND = 2;
SCORE_TYPE_RESULT = 3;

RESULT_STATE_PENDING = 0;
RESULT_STATE_STARTED = 1;
RESULT_STATE_FINISHED = 2;


class Test:
    def __init__(self):
        self.id = -1;
        self._best = Result();
        self._last = Result();
        self._current = Result();
        self._next = Result();
        self._average = 0.0;
        self.units = UNITS_SECONDS;

    def setUnits(self, type):
        self.units = type;

    def setBest(self, result):
        self._best = result;

    def setLast(self, result):
        self._last = result;

    def setCurrent(self, result):
        self._current = result;

    def setNext(self, result):
        self._next = result;

    def setAverage(self, value):
        self._average = value;

    def startTest(self):
        # called when test begins for participant. Usually begins with an indentity score
        return;

    def endTest(self):
        # called when test is complete. Either some time after end of run, when next participant starts, or after a timeout.
        return;

    def startRun(self):
        # called when a SCORE_TYPE_RUNSTART is recieved. Used to send signals/data to external screens/sources for start
        return;

    def endRun(self):
        # called when a SCORE_TYPE_RUNEND or SCORE_TYPE_RESULT is recieved.
        return;

    def newDataRecieved(self, score):
        if (score.type == SCORE_TYPE_INDENTIFY):
            self._current.key = score.key;
            self._current.test = self.id;
            self.self.startTest();
        elif (score.type == SCORE_TYPE_RUNSTART):
            self._current.key = score.key;
            self._current.value = score.value;
            self._current.units = score.units;
            self._current.test = self.id;
            self._current.state = RESULT_STATE_STARTED;
            self.startRun();
        elif (score.type == SCORE_TYPE_RUNEND):
            if (
                            self._current.key == score.key and self._current.units == score.units and self._current.test == self.id and self._current.state == RESULT_STATE_STARTED):
                self._current.state = RESULT_STATE_FINISHED;
                self._current.value -= score.value;
                self.endRun();
                self.schedule_endTest();
        elif (score.type == SCORE_TYPE_RESULT):
            self._current.key = score.key;
            self._current.value = score.value;
            self._current.units = score.units;
            self._current.test = self.id;
            self._current.state = RESULT_STATE_FINISHED;
            self.endRun();
            self.schedule_endTest();


class Result:  ##CALCULATIONS
    def __init__(self):
        self.id = -1;
        self.key = '';
        self.value = 0;
        self.units = '';
        self.test = '';
        self.state = RESULT_STATE_PENDING;


class Score:  ##RAW INPUT
    def __init__(self):
        self.id = -1;
        self.type = SCORE_TYPE_INDENTIFY;
        self.value = 0;
        self.key = '';
        self.units = UNITS_SECONDS;





