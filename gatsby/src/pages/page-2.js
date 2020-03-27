import React from "react"
// import { Link } from "gatsby"
import { Row, Col } from "react-bootstrap"

import Layout from "../components/layout"
import SEO from "../components/seo"

const SecondPage = () => (
  <Layout pageInfo={{ pageName: "page-2" }}>
    <SEO title="Datasource and Copyright" />
    <Row>
      <Col>
        <h1>Datasource and Copyright</h1>
        <p>
          All charts on this page a generated on the basis of data provided by the data repository for the 2019 Novel Coronavirus Visual Dashboard operated by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE). Also, Supported by ESRI Living Atlas Team and the Johns Hopkins University Applied Physics Lab (JHU APL).
          This data is provided here: <a href="https://github.com/CSSEGISandData/COVID-19" taget="_blank">https://github.com/CSSEGISandData/COVID-19</a>
        </p>
      </Col>
    </Row>
    <Row>
      <Col>
        <h4>
          The Johns Hopkins University states on their <a href="https://github.com/CSSEGISandData/COVID-19" target="_blank">GitHub Repository</a>:
        </h4>
        <p>
          <strong>Terms of Use (Original Data):</strong><br />
          This GitHub repo and its contents herein, including all data, mapping, and analysis, copyright 2020 Johns Hopkins University, all rights reserved, is provided to the public strictly for educational and academic research purposes. The Website relies upon publicly available data from multiple sources, that do not always agree. The Johns Hopkins University hereby disclaims any and all representations and warranties with respect to the Website, including accuracy, fitness for use, and merchantability. Reliance on the Website for medical guidance or use of the Website in commerce is strictly prohibited.
        </p>

      </Col>
    </Row>
    <Row>
      <Col>
      <h4>
        Following this strict copyright, I have to put the charts generated and provided here also under the same strict copyright.
      </h4>
        <p>
          <strong>Terms of Use (Charts, this website and the underlying GitHub repo):</strong><br />
          This GitHub repo and its contents herein, including all charts, data, mapping, and analysis, copyright 2020 Felix Kratzer, all rights reserved, is provided to the public strictly for educational and academic research purposes.
          The Website relies upon publicly available data from Johns Hopkins University. We hereby disclaim any and all representations and warranties with respect to the Website, including accuracy, fitness for use, and merchantability.
          Reliance on the Website for medical guidance or use of the Website in commerce is strictly prohibited.

        </p>
      </Col>
    </Row>



  </Layout>
)

export default SecondPage
