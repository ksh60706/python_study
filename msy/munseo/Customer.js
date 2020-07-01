import React from 'react';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell'

class Customer extends React.Component {
    render() {
        return ( 
           
        <TableRow>
        <TableCell>{this.prps.id}</TableCell>
           <TableCell><img src ={this.props.image} alt="profile" /></TableCell>
           <TableCell>{this.prps.name}</TableCell>
           <TableCell>{this.prps.birthday}</TableCell>
           <TableCell>{this.prps.gender}</TableCell>
           <TableCell>{this.prps.job}</TableCell>

         </TableRow>

        )

    }

}


    

export default Customer;