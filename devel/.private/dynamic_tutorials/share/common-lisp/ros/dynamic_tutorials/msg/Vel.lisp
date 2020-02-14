; Auto-generated. Do not edit!


(cl:in-package dynamic_tutorials-msg)


;//! \htmlinclude Vel.msg.html

(cl:defclass <Vel> (roslisp-msg-protocol:ros-message)
  ((linear_vel
    :reader linear_vel
    :initarg :linear_vel
    :type cl:float
    :initform 0.0)
   (angular_vel
    :reader angular_vel
    :initarg :angular_vel
    :type cl:float
    :initform 0.0))
)

(cl:defclass Vel (<Vel>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Vel>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Vel)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dynamic_tutorials-msg:<Vel> is deprecated: use dynamic_tutorials-msg:Vel instead.")))

(cl:ensure-generic-function 'linear_vel-val :lambda-list '(m))
(cl:defmethod linear_vel-val ((m <Vel>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dynamic_tutorials-msg:linear_vel-val is deprecated.  Use dynamic_tutorials-msg:linear_vel instead.")
  (linear_vel m))

(cl:ensure-generic-function 'angular_vel-val :lambda-list '(m))
(cl:defmethod angular_vel-val ((m <Vel>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dynamic_tutorials-msg:angular_vel-val is deprecated.  Use dynamic_tutorials-msg:angular_vel instead.")
  (angular_vel m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Vel>) ostream)
  "Serializes a message object of type '<Vel>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'linear_vel))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'angular_vel))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Vel>) istream)
  "Deserializes a message object of type '<Vel>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'linear_vel) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angular_vel) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Vel>)))
  "Returns string type for a message object of type '<Vel>"
  "dynamic_tutorials/Vel")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Vel)))
  "Returns string type for a message object of type 'Vel"
  "dynamic_tutorials/Vel")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Vel>)))
  "Returns md5sum for a message object of type '<Vel>"
  "4798be5c355a1844fc4eb8549a932b03")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Vel)))
  "Returns md5sum for a message object of type 'Vel"
  "4798be5c355a1844fc4eb8549a932b03")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Vel>)))
  "Returns full string definition for message of type '<Vel>"
  (cl:format cl:nil "float32 linear_vel ~%float32 angular_vel~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Vel)))
  "Returns full string definition for message of type 'Vel"
  (cl:format cl:nil "float32 linear_vel ~%float32 angular_vel~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Vel>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Vel>))
  "Converts a ROS message object to a list"
  (cl:list 'Vel
    (cl:cons ':linear_vel (linear_vel msg))
    (cl:cons ':angular_vel (angular_vel msg))
))
