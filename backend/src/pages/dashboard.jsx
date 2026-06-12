import { useEffect, useState } from "react";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer
} from "recharts";

import api from "../api/axios";


function Dashboard() {

  const [data, setData] = useState([]);

  useEffect(() => {

    fetchStats();

  }, []);


  const fetchStats = async () => {

    try {

      const res = await api.get("/analytics/stats");

      setData(res.data);

    } catch (err) {

      console.log(err);

    }

  };


  return (

    <div style={{ padding: "40px" }}>

      <h1>AI Detection Dashboard 🚀</h1>

      <h3>Real Similarity Analytics</h3>

      <div style={{ width: "100%", height: 400 }}>

        <ResponsiveContainer>

          <BarChart data={data}>

            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="name" />

            <YAxis />

            <Tooltip />

            <Bar dataKey="similarity" />

          </BarChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}

export default Dashboard;

<a
  href={`http://localhost:8000/${result.highlighted_pdf}`}
  target="_blank"
  rel="noreferrer"
  className="bg-blue-600 text-white px-4 py-2 rounded inline-block mt-4"
>
  Download Highlighted PDF
</a>