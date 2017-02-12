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
    def __init__():
        id            = -1;
        _best         = Result();
        _last         = Result();
        _current      = Result();
        _next         = Result();
        _average      = 0.0;
        units         = UNITS_SECONDS;
    
    def setUnits( type ):
        units = type;
    
    def setBest( result ):
        _best = result;
    
    def setLast( result ):
        _last = result;
    
    def setCurrent( result ):
        _current = result;
    
    def setNext( result ):
        _next = result;
    
    def setAverage( value ):
        _average = value;
    
    def startTest():
    #called when test begins for participant. Usually begins with an indentity score
    
    def endTest():
    #called when test is complete. Either some time after end of run, when next participant starts, or after a timeout.
    
    def startRun():
    #called when a SCORE_TYPE_RUNSTART is recieved. Used to send signals/data to external screens/sources for start
    
    def endRun():
    #called when a SCORE_TYPE_RUNEND or SCORE_TYPE_RESULT is recieved.
    
    
    

    def newDataRecieved( score ):
        if ( score.type == SCORE_TYPE_INDENTIFY ):
            _current.key = score.key;
            _current.test = self.id;
            self.startTest();
        else if ( score.type == SCORE_TYPE_RUNSTART ):
            _current.key = score.key;
            _current.value = score.value;
            _current.units = score.units;
            _current.test = self.id;
            _current.state = RESULT_STATE_STARTED;
            self.startRun();
        else if ( score.type == SCORE_TYPE_RUNEND ):
            if ( _current.key = score.key and
                _current.units = score.units and
                _current.test = self.id and
                _current.state = RESULT_STATE_STARTED ):
                _current.state = RESULT_STATE_FINISHED;
                _current.value -= score.value;
                self.endRun();
                self.schedule_endTest();
        else if ( score.type == SCORE_TYPE_RESULT ):
            _current.key = score.key;
            _current.value = score.value;
            _current.units = score.units;
            _current.test = self.id;
            _current.state = RESULT_STATE_FINISHED;
            self.endRun();
            self.schedule_endTest();





class Result:       ##CALCULATIONS
    def __init__():
        id = -1;
        key = '';
        value = 0;
        units = '';
        test = '';
        state = RESULT_STATE_PENDING;



class Score:        ##RAW INPUT
    def __init__():
        id = -1;
        type = SCORE_TYPE_INDENTIFY;
        value = 0;
        key = '';
        units = UNITS_SECONDS;





