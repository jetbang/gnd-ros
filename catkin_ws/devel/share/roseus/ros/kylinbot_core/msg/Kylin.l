;; Auto-generated. Do not edit!


(when (boundp 'kylinbot_core::Kylin)
  (if (not (find-package "KYLINBOT_CORE"))
    (make-package "KYLINBOT_CORE"))
  (shadow 'Kylin (find-package "KYLINBOT_CORE")))
(unless (find-package "KYLINBOT_CORE::KYLIN")
  (make-package "KYLINBOT_CORE::KYLIN"))

(in-package "ROS")
;;//! \htmlinclude Kylin.msg.html


(defclass kylinbot_core::Kylin
  :super ros::object
  :slots (_frame_id _cbus ))

(defmethod kylinbot_core::Kylin
  (:init
   (&key
    ((:frame_id __frame_id) 0)
    ((:cbus __cbus) (instance kylinbot_core::CBUS :init))
    )
   (send-super :init)
   (setq _frame_id (round __frame_id))
   (setq _cbus __cbus)
   self)
  (:frame_id
   (&optional __frame_id)
   (if __frame_id (setq _frame_id __frame_id)) _frame_id)
  (:cbus
   (&rest __cbus)
   (if (keywordp (car __cbus))
       (send* _cbus __cbus)
     (progn
       (if __cbus (setq _cbus (car __cbus)))
       _cbus)))
  (:serialization-length
   ()
   (+
    ;; uint32 _frame_id
    4
    ;; kylinbot_core/CBUS _cbus
    (send _cbus :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint32 _frame_id
       (write-long _frame_id s)
     ;; kylinbot_core/CBUS _cbus
       (send _cbus :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint32 _frame_id
     (setq _frame_id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; kylinbot_core/CBUS _cbus
     (send _cbus :deserialize buf ptr-) (incf ptr- (send _cbus :serialization-length))
   ;;
   self)
  )

(setf (get kylinbot_core::Kylin :md5sum-) "29e193a426cfd4a42ee5c1e79efd2ba8")
(setf (get kylinbot_core::Kylin :datatype-) "kylinbot_core/Kylin")
(setf (get kylinbot_core::Kylin :definition-)
      "uint32 frame_id
CBUS cbus

================================================================================
MSG: kylinbot_core/CBUS
uint32 fs
int32 px
int32 py
int32 pz
int16 pe
int16 pc
int16 vx
int16 vy
int16 vz
int16 ve
int16 vc

")



(provide :kylinbot_core/Kylin "29e193a426cfd4a42ee5c1e79efd2ba8")


