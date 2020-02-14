;; Auto-generated. Do not edit!


(when (boundp 'dynamic_tutorials::Vel)
  (if (not (find-package "DYNAMIC_TUTORIALS"))
    (make-package "DYNAMIC_TUTORIALS"))
  (shadow 'Vel (find-package "DYNAMIC_TUTORIALS")))
(unless (find-package "DYNAMIC_TUTORIALS::VEL")
  (make-package "DYNAMIC_TUTORIALS::VEL"))

(in-package "ROS")
;;//! \htmlinclude Vel.msg.html


(defclass dynamic_tutorials::Vel
  :super ros::object
  :slots (_linear_vel _angular_vel ))

(defmethod dynamic_tutorials::Vel
  (:init
   (&key
    ((:linear_vel __linear_vel) 0.0)
    ((:angular_vel __angular_vel) 0.0)
    )
   (send-super :init)
   (setq _linear_vel (float __linear_vel))
   (setq _angular_vel (float __angular_vel))
   self)
  (:linear_vel
   (&optional __linear_vel)
   (if __linear_vel (setq _linear_vel __linear_vel)) _linear_vel)
  (:angular_vel
   (&optional __angular_vel)
   (if __angular_vel (setq _angular_vel __angular_vel)) _angular_vel)
  (:serialization-length
   ()
   (+
    ;; float32 _linear_vel
    4
    ;; float32 _angular_vel
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _linear_vel
       (sys::poke _linear_vel (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _angular_vel
       (sys::poke _angular_vel (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _linear_vel
     (setq _linear_vel (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _angular_vel
     (setq _angular_vel (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get dynamic_tutorials::Vel :md5sum-) "4798be5c355a1844fc4eb8549a932b03")
(setf (get dynamic_tutorials::Vel :datatype-) "dynamic_tutorials/Vel")
(setf (get dynamic_tutorials::Vel :definition-)
      "float32 linear_vel 
float32 angular_vel
")



(provide :dynamic_tutorials/Vel "4798be5c355a1844fc4eb8549a932b03")


