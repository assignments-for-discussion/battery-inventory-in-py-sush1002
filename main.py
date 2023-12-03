
def count_batteries_by_health(present_capacities):
  health_dict={"healthy":0,"exchange":0,"failed":0}  # an empty dictionary to keep track of healthy,exchange and failed batteries
  rated_capacity=120  # the rated capacity of the new battery(given)
  for k in present_capacities:
    soh=(k/rated_capacity)*100
    if soh>80 and soh<=100:
      health_dict["healthy"]+=1
    elif soh>62 and soh<=80:
      health_dict["exchange"]+=1
    elif soh<=62 and soh>=0:
      health_dict["failed"]+=1
  return health_dict
  

  return {  # this is incorrect because here they didnt calculate soh
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
