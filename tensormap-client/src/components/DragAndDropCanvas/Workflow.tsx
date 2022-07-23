import * as React   from 'react'
import BodyWidget from './components/BodyWidget'
import { Application } from "./Application";
import "../DragAndDropCanvas/components/sass/workflow.scss";

class Workflow extends React.Component {

  render() {
    var app = new Application();
    return (
        <BodyWidget app={app} />
    )
  }
}

export default Workflow