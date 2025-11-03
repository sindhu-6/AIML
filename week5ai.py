P_burglary=0.002
P_earthquake=0.001

P_alarm_given_burglary_and_earthquake=0.94
P_alarm_given_burglary_and_no_earthquake=0.95
P_alarm_given_no_burglary_and_earthquake=0.31
P_alarm_given_no_burglary_and_no_earthquake=0.001


P_david_calls_given_alarm=0.91
P_david_does_not_call_given_alarm=0.09
P_david_calls_given_no_alarm=0.05
P_david_does_not_call_given_no_alarm=0.95


P_sophia_calls_given_alarm=0.75
P_sophia_does_not_call_given_alarm=0.25
P_sophia_calls_given_no_alarm=0.02
P_sophia_does_not_call_given_no_alarm=0.98


def joint_probability(alarm,burglary,earthquake,david_calls,sophia_calls):
    if alarm:
        if burglary and earthquake:
            P_alarm=P_alarm_given_burglary_and_earthquake
        elif burglary:
            P_alarm=P_alarm_given_burglary_and_no_earthquake
        elif earthquake:
            P_alarm=P_alarm_given_no_burglary_and_earthquake
        else:
             P_alarm=P_alarm_given_no_burglary_and_no_earthquake
    else:
        if burglary and earthquake:
            P_alarm=1-P_alarm_given_burglary_and_eartquake
        elif burglary:
            P_alarm=1-P_alarm_given_burglary_and_no_earthquake
        elif earthquake:
            P_alarm=1-P_alarm_given_no_burglary_and_earthquake
        else:
             P_alarm=1-P_alarm_given_no_burglary_and_no_earthquake
    P_david=(P_david_calls_given_alarm if david_calls else P_david_does_not_call_given_alarm) if alarm else (P_david_calls_given_no_alarm if david_calls else P_david_does_not_call_given_no_alarm)
    P_sophia=(P_sophia_calls_given_alarm if sophia_calls else P_sophia_does_not_call_given_alarm) if alarm else (P_sophia_calls_given_no_alarm if sophia_calls else P_sophia_does_not_call_given_no_alarm)
    return (P_burglary if burglary else 1-P_burglary)*(P_eartquake if earthquake else 1-P_earthquake)*P_alarm*P_david*P_sophia
result=joint_probability(
    alarm=True,
    burglary=False,
    earthquake=False,
    david_calls=True,
    sophia_calls=True
    )
print(f'The probability that the alarm has sounded ,there is neither a burglary nor an earthquake ,and both david and sophia called harry is:{result:.8f}')
