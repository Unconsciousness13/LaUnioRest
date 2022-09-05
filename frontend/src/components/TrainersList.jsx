import React from "react";
import { useEffect, useState } from "react";
import * as TrainerList from "./TrainersServer";

export default function TrainersList() {
  const [trainers, setTrainers] = useState([]);
  const trainersList = async () => {
    try {
      const res = await TrainerList.trainersList();
      const data = await res.json();
      setTrainers(data);
    } catch (err) {
      console.log(err);
    }
  };

  useEffect(() => {
    trainersList(trainers);
  }, []);
  return (
    <div>
      {trainers.map((trainer) => (
        <div>
          <p>{trainer.first_name}</p>
          <p>{trainer.last_name}</p>
          <p>{trainer.train}</p>
          <p>{trainer.birthdate}</p>
          <p>{trainer.description}</p>
          <img style={{width: '300px', height: '200px'}} src={"https://res.cloudinary.com/hifaleo6q/" + trainer.photo} alt="trainer" />
        </div>
      ))}
    </div>
  );
}
