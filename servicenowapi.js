(function process(/*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {
    try {
        var body = request.body.data;
        gs.info('Received EC2 update: ' + JSON.stringify(body));

        var gr = new GlideRecord('u_ec2_instance_state');
        gr.initialize();
        gr.u_instance_id = body.detail['instance-id'];
        gr.u_state = body.detail.state;
        gr.u_region = body.region;
        gr.u_time_received = new GlideDateTime();
        gr.insert();

        response.setStatus(200);
        response.setBody({ status: 'success', instance_id: gr.u_instance_id });
    } catch (e) {
        gs.error('Error inserting EC2 data: ' + e.message);
        response.setStatus(500);
        response.setBody({ status: 'error', message: e.message });
    }
})(request, response);
