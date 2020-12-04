/*
 * File: c:\Projects\KENYA ONE PROJECT\Frontend-Electron\src\InitialValues.js
 * Project: c:\Projects\KENYA ONE PROJECT\Frontend-Electron
 * Created Date: Friday, January 24th 2020, 8:11:26 pm
 * Author: Geoffrey Nyaga Kinyua ( <info@geoffreynyaga.com> )
 * -----
 * Last Modified: Tuesday November 17th 2020 12:05:47 pm
 * Modified By:  Geoffrey Nyaga Kinyua ( <info@geoffreynyaga.com> )
 * -----
 * MIT License
 *
 * Copyright (c) 2020 KENYA ONE PROJECT
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of
 * this software and associated documentation files (the "Software"), to deal in
 * the Software without restriction, including without limitation the rights to
 * use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
 * of the Software, and to permit persons to whom the Software is furnished to do
 * so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 * -----
 * Copyright (c) 2020 KENYA ONE PROJECT
 */

// const fetchMTOWPlot = () => {
//   fetch("http://localhost:8000/api/accounts/example/", {
//     method: "POST", // or 'PUT'
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({
//       yAxisLimits: context,
//       xAxisLimits: context,
//       aircraft_type: aircraft_type,
//       altitude: altitude,
//       pax: pax,
//       propellerEfficiency: propellerEfficiency,
//       range: range,
//       aspectRatio: aspectRatio,
//       crew: crew,
//     }),
//   })
//     .then((response) => response.json())
//     .then((serverData) => {
//       console.log(" step 2, data from server:", serverData);

//       setIsLoading(false);
//       handleLangChange(serverData);
//     })
//     .catch((error) => {
//       console.log(error, "error in fetchMTOWPlot");
//     });
// };
import React, { useState, useEffect, useContext } from "react";
import useSWR, { mutate } from "swr";

import {
  Card,
  CardHeader,
  CardTitle,
  CardBody,
  Button,
  Form,
  FormInput,
  FormGroup,
  FormSelect,
} from "shards-react";

import { useSelector } from "react-redux";

import { ServerData } from "./types";

const InitialValues = (props) => {
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [yAxisLimits, setYAxisLimits] = useState<number[]>(props.axisRange);
  const [xAxisLimits, setXAxisLimits] = useState<number[]>(props.axisRange);
  const [aircraft_type, setAircraftType] = useState<string>("GA_Twin");
  const [altitude, setAltitude] = useState<number>(10000);
  const [pax, setPax] = useState<number>(4);
  const [propellerEfficiency, setPropellerEfficiency] = useState<number>(0.78);
  const [range, setRange] = useState<number>(1200);
  const [aspectRatio, setAspectRatio] = useState<number>(7.8);
  const [crew, setCrew] = useState<number>(2);
  const [data1, setData1] = useState<null | number[]>(null);

  const sliderValueRedux: number[] = useSelector((state) => state.sliderValue);

  var bodyValues = {
    yAxisLimits: sliderValueRedux,
    xAxisLimits: sliderValueRedux,
    aircraft_type: aircraft_type,
    altitude: altitude,
    pax: pax,
    propellerEfficiency: propellerEfficiency,
    range: range,
    aspectRatio: aspectRatio,
    crew: crew,
  };

  console.log(bodyValues, "[[[[[[[[[[[[[");

  const post = (url: string, x: {}) => {
    console.log("in get", x);

    var lookupOptions = {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        // Authorization: "Token " + token,
      },
      body: JSON.stringify(x),
    };
    return fetch(url, lookupOptions).then((response) => {
      return response.json();
    });
  };

  const loadGroupsTrending = (x = bodyValues) => {
    const endPoint = "http://localhost:8000/api/accounts/example/";

    console.log(sliderValueRedux, data1, x, "loadGroupsTrending");
    return post(endPoint, x);
  };

  const { data, error } = useSWR("loadGroupsTrending", loadGroupsTrending);

  const handleLangChange = (serverData: ServerData) => {
    // console.log(serverData, "step 3, passing to parent");
    props.getChildData(serverData);
  };

  if (data !== undefined) {
    handleLangChange(data);
  }

  // useEffect(() => {
  //   console.log(
  //     " UseEffect: InitialValues ----------",
  //     props.axisRange,
  //     "InitialValues: axis values have changed ----"
  //   );

  //   // setIsLoading(true);
  //   // fetchMTOWPlot();

  // }, [props.axisRange]);

  useEffect(() => {
    console.log(data1, sliderValueRedux, "-useEffect 2");

    // console.log("mutating....");
    if (sliderValueRedux !== data1) {
      setData1(sliderValueRedux);
      mutate("loadGroupsTrending");
    }

    console.log(data1, "- + - useEffect for mutate");
  }, [sliderValueRedux]);

  if (error) return <div>failed to load: {JSON.stringify(error)}</div>;
  if (!data) return <div>loading...</div>;

  if (sliderValueRedux !== data1) {
    console.log(sliderValueRedux, "y2y2y2y2y2y2y2y2y2y2y2yyyyyyyy");

    setData1(sliderValueRedux);
  }

  return (
    <Card>
      {/* <p>{data !== undefined ? JSON.stringify(data) : "undefined"}</p> */}
      <p>data1: {data1}</p>
      <p>sliderValueRedux: {sliderValueRedux}</p>

      <CardHeader>
        <CardTitle>Initial Estimates</CardTitle>
      </CardHeader>
      {/* <h2>{isLoading ? "Loading" : "Not Loading"}</h2> */}
      <CardBody>
        <Form>
          {/* Selected Aircraft */}
          <label htmlFor="#aircraftType">Aircraft Type</label>
          <FormSelect
            onChange={(e: any) => {
              setAircraftType(e.target.value);
              // setIsLoading(false);
            }}
          >
            <option value="SailPlane_Unpowered">SailPlane (Unpowered)</option>
            <option value="SailPlane_Powered">SailPlane (Powered)</option>
            <option value="Homebuilt_Metal_or_Wood">
              Homebuilt - Metal/Wood.
            </option>
            <option value="Homebuilt_Composite">Homebuilt - Composite</option>
            <option value="GA_Single">General Aviation - Single Engine</option>
            <option value="GA_Twin">General Aviation - Twin Engine</option>
            <option value="Agricultural">Agricultural</option>
            <option value="Twin_Turboprop">Twin Turboprop</option>
            <option value="Flying_Boat">Flying Boat</option>
            <option value="Jet_Trainer">Jet Trainer</option>
            <option value="Jet_Fighter">Jet Fighter</option>
            <option value="Military_cargo_or_bomber">
              Military (cargo/bomber)
            </option>
            <option value="Jet_Transport">Jet Transport</option>
          </FormSelect>

          {/* Passengers */}
          <FormGroup>
            <label htmlFor="#pax">Passengers</label>
            <FormInput
              type="number"
              id="#pax"
              placeholder="Number of Passengers"
              // value={2}
              onChange={(e: any) => {
                e.preventDefault();
                setPax(parseInt(e.target.value));
              }}
            />
          </FormGroup>

          {/* Range */}
          <FormGroup>
            <label htmlFor="#range">Range</label>
            <FormInput
              type="number"
              id="#range"
              placeholder="Range (kms)"
              onChange={(e: any) => {
                e.preventDefault();
                setRange(parseInt(e.target.value));
              }}
            />
          </FormGroup>

          {/* Estimated Propeller efficiency */}
          <FormGroup>
            <label htmlFor="#propellerEfficiency">
              Estimated Propeller efficiency
            </label>
            <FormInput
              type="number"
              id="#propellerEfficiency"
              placeholder="Estimated Propeller efficiency (.45 - .85)"
              onChange={(e: any) => {
                e.preventDefault();
                setPropellerEfficiency(parseFloat(e.target.value));
              }}
            />
          </FormGroup>

          {/* Cruise Altitude */}
          <FormGroup>
            <label htmlFor="#altitude">Cruise Altitude</label>
            <FormInput
              type="number"
              id="#altitude"
              placeholder="Cruise Altitude (ft)"
              onChange={(e: any) => {
                e.preventDefault();
                setAltitude(parseInt(e.target.value));
              }}
            />
          </FormGroup>
          {/* Crew */}
          <FormGroup>
            <label htmlFor="#crew">Crew</label>
            <FormInput
              type="number"
              id="#crew"
              placeholder="Number of crew"
              onChange={(e: any) => {
                e.preventDefault();
                setCrew(parseInt(e.target.value));
              }}
            />
          </FormGroup>

          {/* Aspect Ratio */}
          <FormGroup>
            <label htmlFor="#aspectRatio">Aspect Ratio</label>
            <FormInput
              type="number"
              id="#aspectRatio"
              placeholder="Aspect Ratio (6-8)"
              onChange={(e: any) => {
                e.preventDefault();
                setAspectRatio(parseFloat(e.target.value));
              }}
            />
          </FormGroup>
        </Form>

        {/* <Button>SUBMIT</Button> */}

        <Button
          onClick={() => {
            // setIsLoading(true);
            // fetchMTOWPlot();
            mutate("loadGroupsTrending");
          }}
        >
          SUBMIT
        </Button>
      </CardBody>
    </Card>
  );
};

export default InitialValues;
